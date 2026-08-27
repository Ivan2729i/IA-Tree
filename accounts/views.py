from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount
from .forms import (
    AccountProfileForm,
    DeleteAccountConfirmForm,
    DeleteAccountRequestForm,)
from .services.account_deletion_service import AccountDeletionService
from .services.account_deletion_token import (
    create_delete_account_token,
    validate_delete_account_token,)



@login_required
def settings_view(request):
    if request.method == "POST":
        form = AccountProfileForm(
            request.POST,
            instance=request.user,
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Configuración guardada correctamente.",
            )

            return redirect("accounts:settings")

    else:
        form = AccountProfileForm(
            instance=request.user,
        )

    email_verified = EmailAddress.objects.filter(
        user=request.user,
        email__iexact=request.user.email,
        verified=True,
    ).exists()

    social_accounts = SocialAccount.objects.filter(
        user=request.user,
    )

    context = {
        "active_nav": "settings",
        "form": form,
        "email_verified": email_verified,
        "social_accounts": social_accounts,
    }

    return render(
        request,
        "account/settings.html",
        context,
    )


@login_required
def delete_account_request(request):
    if request.method == "POST":
        form = DeleteAccountRequestForm(
            request.POST,
            user=request.user,
        )

        if form.is_valid():
            token = create_delete_account_token(
                request.user,
            )

            delete_url = request.build_absolute_uri(
                reverse(
                    "accounts:delete_account_confirm",
                    kwargs={
                        "token": token,
                    },
                )
            )

            context = {
                "user": request.user,
                "delete_url": delete_url,
            }

            subject = render_to_string(
                "account/email/account_delete_subject.txt",
                context,
            ).strip()

            text_body = render_to_string(
                "account/email/account_delete_message.txt",
                context,
            )

            html_body = render_to_string(
                "account/email/account_delete_message.html",
                context,
            )

            email = EmailMultiAlternatives(
                subject=subject,
                body=text_body,
                to=[request.user.email],
            )

            email.attach_alternative(
                html_body,
                "text/html",
            )

            email.send()

            messages.success(
                request,
                "Te enviamos un correo para confirmar la eliminación de tu cuenta.",
            )

            return redirect(
                "accounts:delete_account_sent",
            )

    else:
        form = DeleteAccountRequestForm(
            user=request.user,
        )

    return render(
        request,
        "account/delete_account_request.html",
        {
            "active_nav": "settings",
            "form": form,
        },
    )


@login_required
def delete_account_sent(request):
    return render(
        request,
        "account/delete_account_sent.html",
        {
            "active_nav": "settings",
        },
    )


@login_required
def delete_account_confirm(request, token):
    payload = validate_delete_account_token(
        token,
    )

    if not payload:
        return render(
            request,
            "account/delete_account_invalid.html",
            {
                "active_nav": "settings",
            },
        )

    if payload.get("user_id") != request.user.pk:
        return render(
            request,
            "account/delete_account_invalid.html",
            {
                "active_nav": "settings",
            },
        )

    if payload.get("email") != request.user.email:
        return render(
            request,
            "account/delete_account_invalid.html",
            {
                "active_nav": "settings",
            },
        )

    if request.method == "POST":
        form = DeleteAccountConfirmForm(
            request.POST,
        )

        if form.is_valid():
            user = request.user

            logout(request)

            AccountDeletionService.delete_account(
                user,
            )

            messages.success(
                request,
                "Tu cuenta fue eliminada correctamente.",
            )

            return redirect(
                "account_login",
            )

    else:
        form = DeleteAccountConfirmForm()

    return render(
        request,
        "account/delete_account_confirm.html",
        {
            "active_nav": "settings",
            "form": form,
        },
    )
