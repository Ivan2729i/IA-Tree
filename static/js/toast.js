const toastContainer = document.getElementById("toast-container");

const toastStyles = {
    success: {
        icon: "✓",
        classes: "border-emerald-200 bg-white text-emerald-600"
    },
    error: {
        icon: "!",
        classes: "border-red-200 bg-white text-red-600"
    },
    warning: {
        icon: "!",
        classes: "border-amber-200 bg-white text-amber-600"
    },
    info: {
        icon: "i",
        classes: "border-indigo-200 bg-white text-accent"
    }
};


function normalizeType(type) {
    if (!type) return "info";

    if (type.includes("success")) return "success";
    if (type.includes("error")) return "error";
    if (type.includes("warning")) return "warning";

    return "info";
}


window.showToast = function(message, type = "info", duration = 4500) {
    if (!toastContainer || !message) return;

    const normalizedType = normalizeType(type);
    const config = toastStyles[normalizedType];

    const toast = document.createElement("div");

    toast.className = `
        pointer-events-auto flex translate-x-8 items-start gap-3 rounded-xl border
        px-4 py-3 opacity-0 shadow-lg transition-all duration-300
        ${config.classes}
    `;

    toast.innerHTML = `
        <div class="flex h-7 w-7 shrink-0 items-center justify-center rounded-full bg-current/10 text-sm font-bold">
            ${config.icon}
        </div>

        <div class="min-w-0 flex-1 pt-0.5">
            <p class="text-sm font-medium text-slate-800"></p>
        </div>

        <button type="button" class="shrink-0 text-slate-400 transition hover:text-slate-700" aria-label="Cerrar">
            <svg class="h-4 w-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M6 6l12 12M18 6 6 18"/>
            </svg>
        </button>
    `;

    toast.querySelector("p").textContent = message;

    const closeButton = toast.querySelector("button");

    function removeToast() {
        toast.classList.add("translate-x-8", "opacity-0");

        setTimeout(() => {
            toast.remove();
        }, 300);
    }

    closeButton.addEventListener("click", removeToast);

    toastContainer.appendChild(toast);

    requestAnimationFrame(() => {
        toast.classList.remove("translate-x-8", "opacity-0");
    });

    if (duration > 0) {
        setTimeout(removeToast, duration);
    }
};


document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll("[data-toast-message]").forEach(element => {
        const message = element.dataset.toastMessage;
        const type = element.dataset.toastType;

        window.showToast(message, type);
    });
});
