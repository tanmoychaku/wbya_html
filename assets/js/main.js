(() => {
  document.addEventListener("DOMContentLoaded", () => {
    loadSharedLayout()
      .catch((error) => {
        console.error("Unable to load shared site layout.", error);
      })
      .finally(() => {
        setActiveNavigation();
        initNavigation();
        initHeroSlider();
        window.addEventListener("hashchange", setActiveNavigation);
      });
  });

  async function loadSharedLayout() {
    const slots = Array.from(document.querySelectorAll("[data-layout-slot]"));

    if (!slots.length) return;

    const response = await fetch("base.html", { credentials: "same-origin" });

    if (!response.ok) {
      throw new Error(`base.html returned ${response.status}`);
    }

    const html = await response.text();
    const source = new DOMParser().parseFromString(html, "text/html");

    slots.forEach((slot) => {
      const slotName = slot.dataset.layoutSlot;
      const template = source.getElementById(`site-${slotName}-template`);

      if (!template) return;

      slot.replaceWith(template.content.cloneNode(true));
    });
  }

  function initNavigation() {
    const mobileMenu = document.querySelector(".mobile-menu");
    const primaryNav = document.getElementById("primaryNav");

    if (!mobileMenu || !primaryNav) return;

    function closeSubmenus() {
      primaryNav.querySelectorAll(".nav-item.is-open").forEach((item) => {
        item.classList.remove("is-open");
        item.querySelector(".submenu-toggle")?.setAttribute("aria-expanded", "false");
      });
    }

    function closeMobileMenu() {
      primaryNav.classList.remove("is-open");
      mobileMenu.classList.remove("is-open");
      mobileMenu.setAttribute("aria-expanded", "false");
      mobileMenu.textContent = "\u2630";
      closeSubmenus();
    }

    primaryNav.querySelectorAll(".submenu-toggle").forEach((toggle) => {
      toggle.addEventListener("click", (event) => {
        event.stopPropagation();
        const navItem = toggle.closest(".nav-item");
        const isOpen = navItem.classList.toggle("is-open");
        toggle.setAttribute("aria-expanded", String(isOpen));
      });
    });

    mobileMenu.addEventListener("click", () => {
      const isOpen = primaryNav.classList.toggle("is-open");
      mobileMenu.classList.toggle("is-open", isOpen);
      mobileMenu.setAttribute("aria-expanded", String(isOpen));
      mobileMenu.textContent = isOpen ? "\u00d7" : "\u2630";
    });

    primaryNav.querySelectorAll("a").forEach((link) => {
      link.addEventListener("click", closeMobileMenu);
    });

    document.addEventListener("click", (event) => {
      if (!primaryNav.contains(event.target) && !mobileMenu.contains(event.target)) {
        closeSubmenus();
      }
    });

    window.addEventListener("resize", () => {
      if (window.innerWidth > 1100) {
        closeMobileMenu();
      }
    });
  }

  function setActiveNavigation() {
    const currentPage = getPageName(window.location.pathname);
    const currentHash = window.location.hash;
    const memberPages = new Set([
      "office-bearers.html",
      "affiliated-units.html",
      "associate-members.html",
      "life-members.html",
      "registered-players.html",
      "our-pride.html"
    ]);

    document.querySelectorAll(".nav a, .footer-menu a").forEach((link) => {
      const active = isCurrentLink(link, currentPage, currentHash);
      link.classList.toggle("is-active", active);
      link.closest(".menu-item")?.classList.toggle("current-menu-item", active);
    });

    const membersToggle = document.querySelector(".submenu-toggle");
    const activeMemberLink = document.querySelector(".sub-menu a.is-active");
    membersToggle?.classList.toggle("is-active", Boolean(activeMemberLink) || memberPages.has(currentPage));
  }

  function isCurrentLink(link, currentPage, currentHash) {
    const href = link.getAttribute("href");

    if (!href) return false;

    let url;

    try {
      url = new URL(href, window.location.href);
    } catch {
      return false;
    }

    if (url.origin !== window.location.origin) return false;

    const linkPage = getPageName(url.pathname);

    if (currentPage === "index.html") {
      if (linkPage !== "index.html") return false;
      if (currentHash) return url.hash === currentHash;
      return !url.hash;
    }

    return linkPage === currentPage && !url.hash;
  }

  function getPageName(pathname) {
    const name = pathname.split("/").filter(Boolean).pop();
    return name && name.includes(".") ? name : "index.html";
  }

  function initHeroSlider() {
    const slidesData = [
      {
        eyebrow: "Featured Championship",
        title: "47th Senior National Yogasana Sports Championship",
        description: "A professional showcase for championship updates, results, notices and athlete achievements."
      },
      {
        eyebrow: "Golden Jubilee",
        title: "Celebrating 50+ years of Yoga legacy",
        description: "Honouring the Association's long journey since 1972 with a modern digital presentation."
      },
      {
        eyebrow: "Youth Participation",
        title: "Sub-Junior & Junior National Yogasana Sports",
        description: "Dedicated space for young athletes, competition galleries and event information."
      },
      {
        eyebrow: "State Games",
        title: "Netaji Subhas State Games highlights",
        description: "Clean visual storytelling for state-level participation, reports and memorable moments."
      }
    ];

    const slides = Array.from(document.querySelectorAll(".slide"));
    const dotsWrap = document.getElementById("sliderDots");
    const heroEyebrow = document.getElementById("heroEyebrow");
    const heroTitle = document.getElementById("heroTitle");
    const heroDescription = document.getElementById("heroDescription");

    if (!slides.length || !dotsWrap || !heroEyebrow || !heroTitle || !heroDescription) return;

    let currentSlide = 0;
    let timer;

    slidesData.forEach((_, index) => {
      const dot = document.createElement("button");
      dot.className = index === 0 ? "dot is-active" : "dot";
      dot.setAttribute("aria-label", `Show slide ${index + 1}`);
      dot.addEventListener("click", () => {
        showSlide(index);
        restartSlider();
      });
      dotsWrap.appendChild(dot);
    });

    const dots = Array.from(document.querySelectorAll(".dot"));

    function showSlide(index) {
      currentSlide = index;
      slides.forEach((slide, slideIndex) => {
        const img = slide.querySelector("img");
        slide.classList.toggle("is-active", slideIndex === index);

        if (img) {
          img.style.animation = "none";
          void img.offsetHeight;
          img.style.animation = "";
        }
      });

      dots.forEach((dot, dotIndex) => {
        dot.classList.toggle("is-active", dotIndex === index);
      });

      const data = slidesData[index];
      heroEyebrow.textContent = data.eyebrow;
      heroTitle.textContent = data.title;
      heroDescription.textContent = data.description;
    }

    function nextSlide() {
      showSlide((currentSlide + 1) % slides.length);
    }

    function startSlider() {
      timer = window.setInterval(nextSlide, 5200);
    }

    function restartSlider() {
      window.clearInterval(timer);
      startSlider();
    }

    startSlider();
  }
})();
