document.addEventListener("DOMContentLoaded", function () {
  const menuItems = document.querySelectorAll(".menu-item");

  function setActiveMenuItem() {
    const currentPath = window.location.pathname;

    menuItems.forEach(function (item) {
      const submenu = item.nextElementSibling;
      const links = submenu ? submenu.querySelectorAll("a") : [];

      links.forEach(function (link) {
        if (link.getAttribute("href") === currentPath) {
          item.classList.add("active");
          submenu.classList.add("active");
          link.classList.add("active");
        }
      });
    });
  }

  menuItems.forEach(function (item) {
    item.addEventListener("click", function () {
      const isActive = this.classList.contains("active");
      const submenu = this.nextElementSibling;

      menuItems.forEach(function (el) {
        el.classList.remove("active");
        const submenu_aux = el.nextElementSibling;
        if (submenu_aux) {
          submenu_aux.classList.remove("active");
          const links_aux = submenu_aux.querySelectorAll("a");
          links_aux.forEach(function (link) {
            link.classList.remove("active");
          });
        }
      });

      if (!isActive) {
        this.classList.add("active");
        if (submenu) {
          submenu.classList.add("active");
        }
      }
    });
  });

  setActiveMenuItem();
});
