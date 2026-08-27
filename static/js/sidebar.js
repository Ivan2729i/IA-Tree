const sidebar = document.getElementById("sidebar");
const overlay = document.getElementById("sidebar-overlay");

const openButton = document.getElementById("menu-open");
const closeButton = document.getElementById("menu-close");


function openSidebar() {
    if (!sidebar || !overlay) {
        return;
    }

    sidebar.classList.remove("-translate-x-full");
    overlay.classList.remove("hidden");

    document.body.classList.add("overflow-hidden");
}


function closeSidebar() {
    if (!sidebar || !overlay) {
        return;
    }

    sidebar.classList.add("-translate-x-full");
    overlay.classList.add("hidden");

    document.body.classList.remove("overflow-hidden");
}


openButton?.addEventListener("click", openSidebar);

closeButton?.addEventListener("click", closeSidebar);

overlay?.addEventListener("click", closeSidebar);


document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
        closeSidebar();
    }
});
