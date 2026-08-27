document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll("[data-password-toggle]").forEach(button => {
        const targetId = button.dataset.passwordToggle;
        const input = document.getElementById(targetId);

        if (!input) return;

        button.addEventListener("click", () => {
            const visible = input.type === "text";

            input.type = visible ? "password" : "text";

            button.setAttribute(
                "aria-label",
                visible ? "Mostrar contraseña" : "Ocultar contraseña"
            );

            button.querySelector("[data-eye-open]")?.classList.toggle("hidden", !visible);
            button.querySelector("[data-eye-closed]")?.classList.toggle("hidden", visible);
        });
    });
});
