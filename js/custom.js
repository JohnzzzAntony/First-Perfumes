(function ($) {
  "use strict";

  const params = new URLSearchParams(window.location.search);
  const mode = params.get("mode");
  if( mode == 'dark' ) {
    $('body').addClass('dark');
  }
  

  gsap.registerPlugin(ScrollTrigger, ScrollSmoother);
  let smoother = ScrollSmoother.create({
    wrapper: "#smooth-wrapper", // should wrap the whole page
    content: "#smooth-content", // should contain all content
    smooth: 2,
    smoothTouch: 0.1,
    effects: true, // must be true to use data-lag
  });

  $(".sidebar-button").on("click", function () {
    $(this).toggleClass("active");
  });

  const sidebarButton = document.querySelector(".sidebar-button");

  if (sidebarButton) {
    sidebarButton.addEventListener("click", () => {
      document.querySelector(".main-menu").classList.toggle("show-menu");
    });
  }

  $(".menu-close-btn").on("click", function () {
    $(".main-menu").removeClass("show-menu");
  });

  // sidebar
  $(".right-sidebar-button").on("click", function () {
    $(".right-sidebar-menu").addClass("show-right-menu");
  });
  $(".right-sidebar-close-btn").on("click", function () {
    $(".right-sidebar-menu").removeClass("show-right-menu");
  });

  jQuery(".dropdown-icon").on("click", function () {
    jQuery(this)
      .toggleClass("active")
      .next("ul, .mega-menu, .mega-menu2")
      .slideToggle();
    jQuery(this)
      .parent()
      .siblings()
      .children("ul, .mega-menu, .mega-menu2")
      .slideUp();
    jQuery(this).parent().siblings().children(".active").removeClass("active");
  });
  jQuery(".dropdown-icon2").on("click", function () {
    jQuery(this).toggleClass("active").next(".submenu-list").slideToggle();
    jQuery(this).parent().siblings().children(".submenu-list").slideUp();
    jQuery(this).parent().siblings().children(".active").removeClass("active");
  });
  jQuery(function ($) {
    $(document).on("click", ".portfolio-drop-down", function (e) {
      e.preventDefault(); // Prevent default anchor behavior

      let submenu = $(this).siblings(".sub-menu"); // Get submenu

      if (submenu.length) {
        // Close other submenus at the same level
        $(this).parent().siblings().find(".sub-menu").slideUp();

        // Toggle clicked submenu
        submenu.stop(true, true).slideToggle();
      }
    });
  });

  // sticky header
  // window.addEventListener("scroll", function () {
  //   const header = document.querySelector("header.header-area, header.home4-sticky");
  //   if (header) {
  //     header.classList.toggle("sticky", window.scrollY > 0);
  //   }
  // });
  let stickyLock = false; // ✅ video section এ গেলে sticky off থাকবে

  window.addEventListener("scroll", function () {
    const header = document.querySelector(
      "header.header-area, header.home4-sticky",
    );
    if (!header) return;

    if (stickyLock) {
      header.classList.remove("sticky"); // force remove
      return;
    }

    header.classList.toggle("sticky", window.scrollY > 0);
  });

  // FancyBox Js
  $('[data-fancybox="gallery-01"]').fancybox({
    buttons: ["close"],
    loop: false,
    protect: true,
  });
  $(".video-player").fancybox({
    buttons: ["close"],
    loop: false,
    protect: true,
  });
  //Counter up
  $(".counter").counterUp({
    delay: 10,
    time: 1000,
  });

  // Home1 Process Slider
  var swiper = new Swiper(".home1-process-slider", {
    slidesPerView: 1,
    speed: 1500,
    spaceBetween: 60,
    autoplay: {
      delay: 2500, // Autoplay duration in milliseconds
      disableOnInteraction: false,
    },
    navigation: {
      nextEl: ".process-slider-next",
      prevEl: ".process-slider-prev",
    },
    breakpoints: {
      280: {
        slidesPerView: 1,
        spaceBetween: 15,
      },
      386: {
        slidesPerView: 1,
        spaceBetween: 15,
      },
      576: {
        slidesPerView: 1,
        spaceBetween: 15,
      },
      768: {
        slidesPerView: 2,
        spaceBetween: 15,
      },
      992: {
        slidesPerView: 3,
        spaceBetween: 15,
      },
      1200: {
        slidesPerView: 3,
        spaceBetween: 25,
      },
      1400: {
        slidesPerView: 3,
      },
    },
  });

  var swiper = new Swiper(".home1-testimonial-slider", {
    slidesPerView: 1,
    speed: 1500,
    spaceBetween: 30,
    loop: true,
    effect: "fade", // Use the fade effect
    fadeEffect: {
      crossFade: true, // Enable cross-fade transition
    },
    autoplay: {
      delay: 2500, // Autoplay duration in milliseconds
      disableOnInteraction: false,
    },
    pagination: {
      el: ".testimonial-pagi",
      clickable: true,
    },
  });

  // Home3 Banner Slider
  var swiper = new Swiper(".home3-banner-slide", {
    slidesPerView: 1,
    speed: 1500,
    spaceBetween: 30,
    loop: true,
    effect: "fade", // Use the fade effect
    fadeEffect: {
      crossFade: true, // Enable cross-fade transition
    },
    autoplay: {
      delay: 2500, // Autoplay duration in milliseconds
      disableOnInteraction: false,
    },
    pagination: {
      el: ".banner-pagi",
      clickable: true,
    },
  });
  // Home3 team Slider
  var swiper = new Swiper(".team-card-slider", {
    slidesPerView: 1,
    speed: 1500,
    spaceBetween: 60,
    autoplay: {
      delay: 2500, // Autoplay duration in milliseconds
      disableOnInteraction: false,
    },
    pagination: {
      el: ".team-section-pagi",
      clickable: true,
    },
    breakpoints: {
      280: {
        slidesPerView: 1,
        spaceBetween: 15,
      },
      386: {
        slidesPerView: 1,
        spaceBetween: 15,
      },
      576: {
        slidesPerView: 2,
        spaceBetween: 15,
      },
      768: {
        slidesPerView: 2,
        spaceBetween: 15,
      },
      992: {
        slidesPerView: 3,
        spaceBetween: 15,
      },
      1200: {
        slidesPerView: 4,
        spaceBetween: 15,
      },
      1400: {
        slidesPerView: 4,
        spaceBetween: 25,
      },
    },
  });
  var swiper = new Swiper(".creative-team-card-slider", {
    slidesPerView: 1,
    speed: 1500,
    spaceBetween: 60,
    autoplay: {
      delay: 2000, // Autoplay duration in milliseconds
      disableOnInteraction: false,
    },
    pagination: {
      el: ".creative-team-pagi",
      clickable: true,
    },
    breakpoints: {
      280: {
        slidesPerView: 1,
        spaceBetween: 15,
      },
      386: {
        slidesPerView: 1,
        spaceBetween: 15,
      },
      576: {
        slidesPerView: 2,
        spaceBetween: 15,
      },
      768: {
        slidesPerView: 2,
        spaceBetween: 15,
      },
      992: {
        slidesPerView: 3,
        spaceBetween: 15,
      },
      1200: {
        slidesPerView: 4,
        spaceBetween: 15,
      },
      1400: {
        slidesPerView: 4,
        spaceBetween: 25,
      },
    },
  });
  // Home3 Testimonial section
  var swiper = new Swiper(".home3-testimonial-slide", {
    slidesPerView: 1,
    speed: 1500,
    spaceBetween: 60,
    autoplay: {
      delay: 2500, // Autoplay duration in milliseconds
      disableOnInteraction: false,
    },
    pagination: {
      el: ".testimonial-section-pagi",
      clickable: true,
    },
    breakpoints: {
      280: {
        slidesPerView: 1,
        spaceBetween: 15,
      },
      386: {
        slidesPerView: 1,
        spaceBetween: 15,
      },
      576: {
        slidesPerView: 1,
        spaceBetween: 15,
      },
      768: {
        slidesPerView: 1,
        spaceBetween: 15,
      },
      992: {
        slidesPerView: 2,
        spaceBetween: 15,
      },
      1200: {
        slidesPerView: 2,
        spaceBetween: 25,
      },
      1400: {
        slidesPerView: 2,
        spaceBetween: 25,
      },
    },
  });
  // Award slider section
  var swiper = new Swiper(".award-slider", {
    slidesPerView: 1,
    speed: 1500,
    spaceBetween: 60,
    autoplay: {
      delay: 2500, // Autoplay duration in milliseconds
      disableOnInteraction: false,
    },
    pagination: {
      el: ".testimonial-section-pagi",
      clickable: true,
    },
    breakpoints: {
      280: {
        slidesPerView: 1.5,
        spaceBetween: 15,
      },
      386: {
        slidesPerView: 1.5,
        spaceBetween: 15,
      },
      576: {
        slidesPerView: 2.5,
        spaceBetween: 15,
      },
      768: {
        slidesPerView: 3.5,
        spaceBetween: 15,
      },
      992: {
        slidesPerView: 4.5,
        spaceBetween: 15,
      },
      1200: {
        slidesPerView: 5.5,
        spaceBetween: 25,
      },
      1400: {
        slidesPerView: 6.5,
        spaceBetween: 25,
      },
    },
  });
  // Home3 Banner Slider
  var swiper = new Swiper(".portfolio-details-slider", {
    slidesPerView: 1,
    speed: 1500,
    spaceBetween: 30,
    loop: true,
    effect: "fade", // Use the fade effect
    fadeEffect: {
      crossFade: true, // Enable cross-fade transition
    },
    autoplay: {
      delay: 2500, // Autoplay duration in milliseconds
      disableOnInteraction: false,
    },
    pagination: {
      el: ".banner-pagi",
      clickable: true,
    },
    navigation: {
      nextEl: ".slider-next",
      prevEl: ".slider-prev",
    },
  });
  // Home6 Testimonial Slider
	var swiper = new Swiper(".home6-testimonial-slider", {
		slidesPerView: 1,
		speed: 1500,
		spaceBetween: 24,
		autoplay: {
			delay: 2500, // Autoplay duration in milliseconds
			disableOnInteraction: false,
			pauseOnMouseEnter: true,
		},
		navigation: {
			nextEl: ".testimonial-slider-next",
			prevEl: ".testimonial-slider-prev",
		},
		breakpoints: {
		  280: {
			slidesPerView: 1,
		  },
		  386: {
			slidesPerView: 1,
		  },
		  576: {
			slidesPerView: 1,
			spaceBetween: 15,
		  },
		  768: {
			slidesPerView: 1,
			spaceBetween: 15,
		  },
		  992: {
			slidesPerView: 2,
		  },
		  1200: {
			slidesPerView: 2,
		  },
		  1400: {
			slidesPerView: 2,
		  },
		},
	});
  //wow js
  jQuery(window).on("load", function () {
    new WOW().init();
    window.wow = new WOW({
      boxClass: "wow",
      animateClass: "animated",
      offset: 0,
      mobile: true,
      live: true,
      offset: 80,
    });
    window.wow.init();
  });

  // niceSelect
  if ($("select").length) {
    $("select").niceSelect();
  }

  // Language Btn
	$(".language-btn").on("click", function (e) {
		let parent  = $(this).parent();
		parent.find(".language-list").toggleClass("active");
		e.stopPropagation();
	});
	$(document).on("click", function (e) {
		if (!$(e.target).closest(".language-btn" ).length) {
		  $(".language-list").removeClass("active");
		}
	});

  // Dark Light
  const dayNight = document.querySelector(".tt-style-switch");
  const body = document.body;
  const icon = dayNight.querySelector("i");

  const toggleDarkMode = () => {
    body.classList.toggle("dark");

    icon.classList.toggle(
      "bi-brightness-low-fill",
      body.classList.contains("dark"),
    );
    icon.classList.toggle("bi-moon", !body.classList.contains("dark"));

    localStorage.setItem(
      "softro_theme",
      body.classList.contains("dark") ? "dark" : "",
    );
  };

  dayNight.addEventListener("click", toggleDarkMode);

  window.addEventListener("load", () => {
    const savedTheme = localStorage.getItem("softro_theme");
    if (savedTheme === "dark") {
      toggleDarkMode();
    }
  });

  setTimeout(() => {
    const darkClassExists = body.classList.contains('dark');
    if( darkClassExists ) {
      icon.classList.add("bi-brightness-low-fill");
      icon.classList.remove("bi-moon");
    }else{
      icon.classList.remove("bi-brightness-low-fill");
      icon.classList.add("bi-moon");
    }
  }, 500);

  // Text Effect Animation
  if ($(".text-anim").length) {
    let staggerAmount = 0.03,
      translateXValue = 20,
      defaultDelay = 0.25,
      easeType = "power2.out",
      animatedTextElements = document.querySelectorAll(".text-anim");

    animatedTextElements.forEach((element) => {
      // HTML to data-delay
      let delayValue = element.getAttribute("data-delay")
        ? parseFloat(element.getAttribute("data-delay"))
        : defaultDelay;

      let animationSplitText = new SplitText(element, { type: "chars, words" });
      gsap.from(animationSplitText.chars, {
        duration: 1,
        delay: delayValue,
        x: translateXValue,
        autoAlpha: 0,
        stagger: staggerAmount,
        ease: easeType,
        scrollTrigger: { trigger: element, start: "top 85%" },
      });
    });
  }

  if ($("body").not(".is-mobile").hasClass("tt-magic-cursor")) {
    if ($(window).width() > 1024) {
      gsap.config({
        nullTargetWarn: false,
        trialWarn: false,
      });
      $(".magnetic-item").wrap('<div class="magnetic-wrap"></div>');

      if ($("a.magnetic-item").length) {
        $("a.magnetic-item").addClass("not-hide-cursor");
      }

      var $mouse = { x: 0, y: 0 }; // Cursor position
      var $pos = { x: 0, y: 0 }; // Cursor position
      var $ratio = 0.15; // delay follow cursor
      var $active = false;
      var $ball = $("#ball");

      var $ballWidth = 20; // Ball default width
      var $ballHeight = 20; // Ball default height
      var $ballOpacity = 0.5; // Ball default opacity
      var $ballBorderWidth = 2; // Ball default border width

      gsap.set($ball, {
        // scale from middle and style ball
        xPercent: -50,
        yPercent: -50,
        width: $ballWidth,
        height: $ballHeight,
        borderWidth: $ballBorderWidth,
        opacity: $ballOpacity,
      });

      document.addEventListener("mousemove", mouseMove);

      function mouseMove(e) {
        $mouse.x = e.clientX;
        $mouse.y = e.clientY;
      }

      gsap.ticker.add(updatePosition);

      function updatePosition() {
        if (!$active) {
          $pos.x += ($mouse.x - $pos.x) * $ratio;
          $pos.y += ($mouse.y - $pos.y) * $ratio;

          gsap.set($ball, { x: $pos.x, y: $pos.y });
        }
      }

      $(".magnetic-wrap").mousemove(function (e) {
        parallaxCursor(e, this, 2); // magnetic ball = low number is more attractive
        callParallax(e, this);
      });

      function callParallax(e, parent) {
        parallaxIt(e, parent, parent.querySelector(".magnetic-item"), 25); // magnetic area = higher number is more attractive
      }

      function parallaxIt(e, parent, target, movement) {
        var boundingRect = parent.getBoundingClientRect();
        var relX = e.clientX - boundingRect.left;
        var relY = e.clientY - boundingRect.top;

        gsap.to(target, {
          duration: 0.3,
          x: ((relX - boundingRect.width / 2) / boundingRect.width) * movement,
          y:
            ((relY - boundingRect.height / 2) / boundingRect.height) * movement,
          ease: Power2.easeOut,
        });
      }

      function parallaxCursor(e, parent, movement) {
        var rect = parent.getBoundingClientRect();
        var relX = e.clientX - rect.left;
        var relY = e.clientY - rect.top;
        $pos.x =
          rect.left + rect.width / 2 + (relX - rect.width / 2) / movement;
        $pos.y =
          rect.top + rect.height / 2 + (relY - rect.height / 2) / movement;
        gsap.to($ball, { duration: 0.3, x: $pos.x, y: $pos.y });
      }

      // Magic cursor behavior
      // ======================

      // Magnetic item hover.
      $(".magnetic-wrap")
        .on("mouseenter mouseover", function (e) {
          $ball.addClass("magnetic-active");
          gsap.to($ball, { duration: 0.3, width: 70, height: 70, opacity: 1 });
          $active = true;
        })
        .on("mouseleave", function (e) {
          $ball.removeClass("magnetic-active");
          gsap.to($ball, {
            duration: 0.3,
            width: $ballWidth,
            height: $ballHeight,
            opacity: $ballOpacity,
          });
          gsap.to(this.querySelector(".magnetic-item"), {
            duration: 0.3,
            x: 0,
            y: 0,
            clearProps: "all",
          });
          $active = false;
        });

      // Alternative cursor style on hover.
      $(
        ".cursor-alter, .tt-main-menu-list > li > a, .tt-main-menu-list > li > .tt-submenu-trigger > a",
      )
        .not(".magnetic-item") // omit from selection.
        .on("mouseenter", function () {
          gsap.to($ball, {
            duration: 0.3,
            borderWidth: 0,
            opacity: 0.2,
            backgroundColor: "#CCC",
            width: "90px",
            height: "90px",
          });
        })
        .on("mouseleave", function () {
          gsap.to($ball, {
            duration: 0.3,
            borderWidth: $ballBorderWidth,
            opacity: $ballOpacity,
            backgroundColor: "transparent",
            width: $ballWidth,
            height: $ballHeight,
            clearProps: "backgroundColor",
          });
        });

      // Cursor view on hover (data attribute "data-cursor="...").
      $("[data-cursor]").each(function () {
        $(this)
          .on("mouseenter", function () {
            $ball
              .addClass("ball-view")
              .append('<div class="ball-view-inner"></div>');
            $(".ball-view-inner").append($(this).attr("data-cursor"));

            gsap.to($ball, {
              duration: 0.3,
              yPercent: -75,
              padding: "8px 20px", // ✅ instead of fixed width/height
              opacity: 1,
              borderWidth: 0,
              height: "auto", // ✅ allow auto height
            });

            gsap.to(".ball-view-inner", {
              duration: 0.3,
              scale: 1,
              autoAlpha: 1,
            });
          })
          .on("mouseleave", function () {
            gsap.to($ball, {
              duration: 0.3,
              yPercent: -50,
              width: $ballWidth, // back to default circle
              height: $ballHeight,
              opacity: $ballOpacity,
              borderWidth: $ballBorderWidth,
              padding: 0, // ✅ reset padding
            });
            $ball.removeClass("ball-view").find(".ball-view-inner").remove();
          });
        $(this).addClass("not-hide-cursor");
      });

      // Cursor drag on hover (class "cursor-drag"). For Swiper sliders.
      $(".swiper").each(function () {
        if ($(this).parent().attr("data-simulate-touch") === "true") {
          if ($(this).parent().hasClass("cursor-drag")) {
            $(this)
              .on("mouseenter", function () {
                $ball.append('<div class="ball-drag"></div>');
                gsap.to($ball, {
                  duration: 0.3,
                  width: 60,
                  height: 60,
                  opacity: 1,
                });
              })
              .on("mouseleave", function () {
                $ball.find(".ball-drag").remove();
                gsap.to($ball, {
                  duration: 0.3,
                  width: $ballWidth,
                  height: $ballHeight,
                  opacity: $ballOpacity,
                });
              });
            $(this).addClass("not-hide-cursor");

            // Ignore "data-cursor" on hover.
            $(this)
              .find("[data-cursor]")
              .on("mouseenter mouseover", function () {
                $ball.find(".ball-drag").remove();
                return false;
              })
              .on("mouseleave", function () {
                $ball.append('<div class="ball-drag"></div>');
                gsap.to($ball, {
                  duration: 0.3,
                  width: 60,
                  height: 60,
                  opacity: 1,
                });
              });
          }
        }
      });

      // Cursor drag on mouse down / click and hold effect (class "cursor-drag-mouse-down"). For Swiper sliders.
      $(".swiper").each(function () {
        if ($(this).parent().attr("data-simulate-touch") === "true") {
          if ($(this).parent().hasClass("cursor-drag-mouse-down")) {
            $(this)
              .on("mousedown pointerdown", function (e) {
                if (e.which === 1) {
                  // Affects the left mouse button only!
                  gsap.to($ball, {
                    duration: 0.2,
                    width: 60,
                    height: 60,
                    opacity: 1,
                  });
                  $ball.append('<div class="ball-drag"></div>');
                }
              })
              .on("mouseup pointerup", function () {
                $ball.find(".ball-drag").remove();
                if ($(this).find("[data-cursor]:hover").length) {
                } else {
                  gsap.to($ball, {
                    duration: 0.2,
                    width: $ballWidth,
                    height: $ballHeight,
                    opacity: $ballOpacity,
                  });
                }
              })
              .on("mouseleave", function () {
                $ball.find(".ball-drag").remove();
                gsap.to($ball, {
                  duration: 0.2,
                  width: $ballWidth,
                  height: $ballHeight,
                  opacity: $ballOpacity,
                });
              });

            // Ignore "data-cursor" on mousedown.
            $(this)
              .find("[data-cursor]")
              .on("mousedown pointerdown", function () {
                return false;
              });

            // Ignore "data-cursor" on hover.
            $(this)
              .find("[data-cursor]")
              .on("mouseenter mouseover", function () {
                $ball.find(".ball-drag").remove();
                return false;
              });
          }
        }
      });

      // Cursor close on hover.
      $(".cursor-close").each(function () {
        $(this).addClass("ball-close-enabled");
        $(this)
          .on("mouseenter", function () {
            $ball.addClass("ball-close-enabled");
            $ball.append('<div class="ball-close">Close</div>');
            gsap.to($ball, {
              duration: 0.3,
              yPercent: -75,
              width: 80,
              height: 80,
              opacity: 1,
            });
            gsap.from(".ball-close", { duration: 0.3, scale: 0, autoAlpha: 0 });
          })
          .on("mouseleave click", function () {
            $ball.removeClass("ball-close-enabled");
            gsap.to($ball, {
              duration: 0.3,
              yPercent: -50,
              width: $ballWidth,
              height: $ballHeight,
              opacity: $ballOpacity,
            });
            $ball.find(".ball-close").remove();
          });

        // Hover on "cursor-close" inner elements.
        $(
          ".cursor-close a, .cursor-close button, .cursor-close .tt-btn, .cursor-close .hide-cursor",
        )
          .not(".not-hide-cursor") // omit from selection (class "not-hide-cursor" is for global use).
          .on("mouseenter", function () {
            $ball.removeClass("ball-close-enabled");
          })
          .on("mouseleave", function () {
            $ball.addClass("ball-close-enabled");
          });
      });

      // ================================================================
      // Scroll between anchors
      // ================================================================

      $('a[href^="#"]')
        .not('[href$="#"]') // omit from selection
        .not('[href$="#0"]') // omit from selection
        .on("click", function () {
          var target = this.hash;

          // If fixed header position enabled.
          if ($("#tt-header").hasClass("tt-header-fixed")) {
            var $offset = $("#tt-header").height();
          } else {
            var $offset = 0;
          }

          // You can use data attribute (for example: data-offset="100") to set top offset in HTML markup if needed.
          if ($(this).data("offset") != undefined)
            $offset = $(this).data("offset");

          return false;
        });

      // Show/hide magic cursor
      // =======================

      // Hide on hover.
      $(
        "a, button, .tt-btn, .tt-form-control, .tt-form-radio, .tt-form-check, .hide-cursor",
      ) // class "hide-cursor" is for global use.
        .not(".not-hide-cursor") // omit from selection (class "not-hide-cursor" is for global use).
        .not(".cursor-alter") // omit from selection
        .not(".tt-main-menu-list > li > a") // omit from selection
        .not(".tt-main-menu-list > li > .tt-submenu-trigger > a") // omit from selection
        .on("mouseenter", function () {
          gsap.to($ball, { duration: 0.3, scale: 0, opacity: 0 });
        })
        .on("mouseleave", function () {
          gsap.to($ball, { duration: 0.3, scale: 1, opacity: $ballOpacity });
        });

      // Hide on click.
      $("a")
        .not('[target="_blank"]') // omit from selection.
        .not('[href^="#"]') // omit from selection.
        .not('[href^="mailto"]') // omit from selection.
        .not('[href^="tel"]') // omit from selection.
        .not(".lg-trigger") // omit from selection.
        .not(".video-player") // omit from selection.
        .not(".tt-btn-disabled") // omit from selection.
        .on("click", function () {
          gsap.to($ball, { duration: 0.3, scale: 1.3, autoAlpha: 0 });
        });

      // Show/hide on document leave/enter.
      $(document)
        .on("mouseleave", function () {
          gsap.to("#magic-cursor", { duration: 0.3, autoAlpha: 0 });
        })
        .on("mouseenter", function () {
          gsap.to("#magic-cursor", { duration: 0.3, autoAlpha: 1 });
        });

      // Show as the mouse moves.
      $(document).mousemove(function () {
        gsap.to("#magic-cursor", { duration: 0.3, autoAlpha: 1 });
      });
    }
  }
  // Back To Top
  jQuery(function ($) {
    const el = document.getElementById("scroll-percentage");
    const valueEl = document.getElementById("scroll-percentage-value");
    if (!el || !valueEl) return;

    const offset = 50;

    function update() {
      const scrollTop = $(window).scrollTop();
      const docH = $(document).height() - $(window).height();

      const progress = docH > 0 ? Math.min(scrollTop / docH, 1) : 0;
      const pct = Math.round(progress * 100);

      // text
      valueEl.textContent = pct + "%";

      // conic gradient
      // IMPORTANT: conic-gradient needs "deg" or "%" stops
      el.style.background = `conic-gradient(var(--primary-color1) ${pct}%, var(--progress-bg) ${pct}%)`;

      // show/hide
      if (scrollTop > offset) el.classList.add("active");
      else el.classList.remove("active");

      // at 100% show arrow (hide percent)
      if (pct >= 100) el.classList.add("is-complete");
      else el.classList.remove("is-complete");
    }

    update();
    $(window).on("scroll resize", update);

    // click (arrow or anywhere inside)
    $("#scroll-percentage").on("click", function (e) {
      e.preventDefault();
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  });

  // ================================
  // Process list: active add/remove cumulatively on scroll
  // Down scroll => 0..i active
  // Up scroll   => i+1..end inactive
  // Works with ScrollSmoother
  // ================================
  (() => {
    const section = document.querySelector(".home3-process-section");
    if (!section) return;

    const items = gsap.utils.toArray(
      ".home3-process-section .process-list .single-process",
    );
    if (!items.length) return;

    // ✅ ScrollSmoother scroller support
    const smoother = gsap.core.globals().ScrollSmoother?.get?.();
    const scrollerEl = smoother ? smoother.wrapper() : window;

    // set cumulative active up to index
    const setActiveTo = (index) => {
      items.forEach((el, i) => el.classList.toggle("active", i <= index));
    };

    // optional initial state (none active)
    items.forEach((el) => el.classList.remove("active"));

    items.forEach((item, i) => {
      ScrollTrigger.create({
        trigger: item,
        scroller: scrollerEl,
        start: "top 40%", // when item reaches middle-ish
        end: "bottom 60%",
        onEnter: () => setActiveTo(i), // down => add up to i
        onEnterBack: () => setActiveTo(i), // up => keep up to i
        onLeaveBack: () => setActiveTo(i - 1), // up past this item => remove it (and after)
      });
    });

    // if user scrolls above the whole section => clear all
    ScrollTrigger.create({
      trigger: section,
      scroller: scrollerEl,
      start: "top bottom",
      onLeaveBack: () => items.forEach((el) => el.classList.remove("active")),
    });

    ScrollTrigger.refresh();
  })();

  // Home4 Portfolio
  $(function () {
    var width = $(window).width();
    if (width > 991) {
      let cards = gsap.utils.toArray(".portfolioCard");

      let stickDistance = 0;

      let lastCardST = ScrollTrigger.create({
        trigger: cards[cards.length - 1],
        start: "top 100px",
      });

      cards.forEach((card, index) => {
        var scale = 1 - (cards.length - index) * 0.025;
        let scaleDown = gsap.to(card, {
          scale: scale,
          "transform-origin":
            '"50% ' + (lastCardST.start + stickDistance) + '"',
        });

        ScrollTrigger.create({
          trigger: card,
          start: "top 100px",
          end: () => lastCardST.start + stickDistance,
          pin: true,
          pinSpacing: false,
          ease: "none",
          animation: scaleDown,
          toggleActions: "restart none none reverse",
        });
      });
    }
  });

  // portfolio Images
  const portfolioImgItem = document.querySelectorAll(
    ".portfolio-wrap .single-portfolio ",
  );
  function followImageCursor(event, portfolioImgItem) {
    const contentBox = portfolioImgItem.getBoundingClientRect();
    const dx = event.clientX - contentBox.x;
    const dy = event.clientY - contentBox.y;
    portfolioImgItem.children[1].style.transform = `translate(${dx}px, ${dy}px) rotate(-19deg)`;
  }

  portfolioImgItem.forEach((item, i) => {
    item.addEventListener("mousemove", (event) => {
      setInterval(followImageCursor(event, item), 100);
    });
  });

  // Industries Images
  const industriesImgItem = document.querySelectorAll(
    ".industries-wrap .single-industries",
  );
  function followImageCursor(event, industriesImgItem) {
    const contentBox = industriesImgItem.getBoundingClientRect();
    const dx = event.clientX - contentBox.x;
    const dy = event.clientY - contentBox.y;
    industriesImgItem.children[1].style.transform = `translate(${dx}px, ${dy}px) rotate(5deg)`;
  }

  industriesImgItem.forEach((item, i) => {
    item.addEventListener("mousemove", (event) => {
      setInterval(followImageCursor(event, item), 100);
    });
  });

  // Skillbar
  window.onload = () => {
    const bars = document.querySelectorAll(".progress-bar");

    bars.forEach((bar) => {
      // Get the percentage from the data attribute
      const percentage = bar.getAttribute("data-progress");
      // Set the width to trigger the CSS transition
      bar.style.width = percentage;
    });
  };

  // fade Animation
  if ($(".fade_anim").length > 0) {
    gsap.utils.toArray(".fade_anim").forEach((item) => {
      let tp_fade_offset = item.getAttribute("data-fade-offset") || 40,
        tp_duration_value = item.getAttribute("data-duration") || 0.75,
        tp_fade_direction = item.getAttribute("data-fade-from") || "bottom",
        tp_onscroll_value = item.getAttribute("data-on-scroll") || 1,
        tp_delay_value = item.getAttribute("data-delay") || 0.15,
        tp_ease_value = item.getAttribute("data-ease") || "power2.out",
        tp_anim_setting = {
          opacity: 0,
          ease: tp_ease_value,
          duration: tp_duration_value,
          delay: tp_delay_value,
          x:
            tp_fade_direction == "left"
              ? -tp_fade_offset
              : tp_fade_direction == "right"
                ? tp_fade_offset
                : 0,
          y:
            tp_fade_direction == "top"
              ? -tp_fade_offset
              : tp_fade_direction == "bottom"
                ? tp_fade_offset
                : 0,
        };
      if (tp_onscroll_value == 1) {
        tp_anim_setting.scrollTrigger = {
          trigger: item,
          start: "top 85%",
        };
      }
      gsap.from(item, tp_anim_setting);
    });
  }

  //Counter Js
  document.querySelectorAll(".counter_number").forEach((el) => {
    const rawText = el.textContent.trim();
    const finalValue = parseInt(rawText, 10) || 0;

    // 🔍 detect if we should show leading zero
    const hasLeadingZero =
      finalValue >= 10 || (rawText.length > 1 && rawText.startsWith("0"));

    const counter = { value: 0 };

    gsap.to(counter, {
      value: finalValue,
      duration: 0.7,
      ease: "none",
      snap: { value: 1 }, // 🔥 integer steps only
      scrollTrigger: {
        trigger: el,
        start: "top 85%",
        once: true,
      },
      onUpdate: () => {
        let v = counter.value;
        el.textContent = hasLeadingZero && v < 10 ? "0" + v : v;
      },
    });
  });

  var swiper = new Swiper(".home2-testimonial-slider", {
    slidesPerView: 1,
    speed: 1500,
    spaceBetween: 30,
    loop: true,
    effect: "fade", // Use the fade effect
    fadeEffect: {
      crossFade: true, // Enable cross-fade transition
    },
    autoplay: {
      delay: 2500, // Autoplay duration in milliseconds
      disableOnInteraction: false,
    },
    navigation: {
      nextEl: ".testimonial-slider-next",
      prevEl: ".testimonial-slider-prev",
    },
    pagination: {
      el: ".franctional-pagi",
      type: "fraction",
    },
  });

  // Home 3 portfolio card
  const cards = document.querySelectorAll(".single-portfolio2");

  cards.forEach((card) => {
    card.addEventListener("mouseenter", () => {
      cards.forEach((c) => c.classList.remove("active"));
      card.classList.add("active");
    });
  });

  // Our work Hover
  $(".our-work-list ul li").on({
    mouseenter: function () {
      // Remove the 'active' class from all content list items
      $(".our-work-list ul li").removeClass("active");
      // Add the 'active' class to the hovered content list item
      $(this).addClass("active");

      // Get the index of the hovered content list item
      var index = $(this).index();

      // Remove the 'active' class from all image list items in both our-work containers
      $(".our-work-img ul li").removeClass("active");

      // Add the 'active' class to the corresponding image list items in both our-work containers
      $(".our-work-img").each(function () {
        $(this)
          .find("ul li:eq(" + index + ")")
          .addClass("active");
      });
    },
  });

  // webgl images hover animation
  if ($(".shape-hover-item").length) {
    let hoverAnimation__do = function (t, n) {
      let a = new hoverEffect({
        parent: t.get(0),
        intensity: t.data("intensity") || void 0,
        speedIn: t.data("speedin") || void 0,
        speedOut: t.data("speedout") || void 0,
        easing: t.data("easing") || void 0,
        hover: t.data("hover") || void 0,
        image1: n.eq(0).attr("src"),
        image2: n.eq(0).attr("src"),
        displacementImage: t.data("displacement"),
        imagesRatio: n[0].height / n[0].width,
        hover: !1,
      });
      t.closest(".shape-hover-item")
        .on("mouseenter", function () {
          a.next();
        })
        .on("mouseleave", function () {
          a.previous();
        });
    };
    let hoverAnimation = function () {
      $(".shape-hover-img").each(function () {
        let n = $(this);
        let e = n.find("img");
        let i = e.eq(0);
        i[0].complete
          ? hoverAnimation__do(n, e)
          : i.on("load", function () {
              hoverAnimation__do(n, e);
            });
      });
    };
    hoverAnimation();
  }

  // Scroll Down all elements with data-target attribute
  const scrollTriggers = document.querySelectorAll("[data-target]");

  // Define top offset (gap)
  const scrollOffset = 120;

  scrollTriggers.forEach((trigger) => {
    trigger.addEventListener("click", (e) => {
      e.preventDefault();

      const targetSelector = trigger.getAttribute("data-target");
      const scrollTarget = document.querySelector(targetSelector);

      if (scrollTarget) {
        // If GSAP ScrollSmoother is active
        if (typeof smoother !== "undefined") {
          // Scroll with offset
          const targetPosition =
            scrollTarget.getBoundingClientRect().top +
            window.scrollY -
            scrollOffset;
          smoother.scrollTo(targetPosition, true);
        } else {
          // Fallback: native smooth scroll with offset
          const targetPosition =
            scrollTarget.getBoundingClientRect().top +
            window.scrollY -
            scrollOffset;

          window.scrollTo({
            top: targetPosition,
            behavior: "smooth",
          });
        }
      }
    });
  });

  // footer top img area
  // document.addEventListener("DOMContentLoaded", () => {
  //   const contactSection = document.querySelector(".footer-top-btn-area");
  //   const btnArea = document.querySelector(".footer-top-btn-area");

  //   const observerOptions = {
  //     root: null, // Use the viewport as the root
  //     threshold: 0.1, // Trigger when 10% of the section is visible
  //   };

  //   const observer = new IntersectionObserver((entries) => {
  //     entries.forEach((entry) => {
  //       if (entry.isIntersecting) {
  //         btnArea.classList.add("active");
  //       } else {
  //         //   btnArea.classList.remove("active");
  //       }
  //     });
  //   }, observerOptions);

  //   if (contactSection) {
  //     observer.observe(contactSection);
  //   }
  // });
  const mm = gsap.matchMedia();
  mm.add("(min-width: 768px)", () => {
    const contactSection = document.querySelector(".home2-footer-top-section");
    const footerTopWrap = document.querySelector(".footer-top-wrapper");
    if (!contactSection) return;

    ScrollTrigger.create({
      trigger: contactSection, // অথবা ".team-img-page"
      start: "top 80%", // element viewport এ ঢুকলেই
      end: "bottom top", // element শেষ হয়ে বের হলে
      onEnter: () => footerTopWrap.classList.add("active"),
      onEnterBack: () => footerTopWrap.classList.add("active"),
      onLeave: () => footerTopWrap.classList.remove("active"),
      onLeaveBack: () => footerTopWrap.classList.remove("active"),
      // markers: true
    });
  });

  // team img area
  // document.addEventListener("DOMContentLoaded", () => {
  //   const teamImgArea = document.querySelector(".team-img-area");
  //   if (!teamImgArea) return;

  //   const observerOptions = {
  //     root: null,
  //     threshold: 0.2, // 20% visible হলে active (0.1/0.3 ট্রাই করতে পারেন)
  //   };

  //   const observer = new IntersectionObserver((entries) => {
  //     entries.forEach((entry) => {
  //       if (entry.isIntersecting) {
  //         teamImgArea.classList.add("active");
  //       } else {
  //         teamImgArea.classList.remove("active");
  //       }
  //     });
  //   }, observerOptions);

  //   observer.observe(teamImgArea);
  // });

  mm.add("(min-width: 768px)", () => {
    const teamImgArea = document.querySelector(".team-img-area");
    if (!teamImgArea) return;

    ScrollTrigger.create({
      trigger: teamImgArea, // অথবা ".team-img-page"
      start: "top 80%", // element viewport এ ঢুকলেই
      end: "bottom top", // element শেষ হয়ে বের হলে
      onEnter: () => teamImgArea.classList.add("active"),
      onEnterBack: () => teamImgArea.classList.add("active"),
      onLeave: () => teamImgArea.classList.remove("active"),
      onLeaveBack: () => teamImgArea.classList.remove("active"),
      // markers: true
    });
  });

  // Home3 award Hover
  $(".award-list ul li").on({
    mouseenter: function () {
      // Remove the 'active' class from all content list items
      $(".award-list ul li").removeClass("active");
      // Add the 'active' class to the hovered content list item
      $(this).addClass("active");

      // Get the index of the hovered content list item
      var index = $(this).index();

      // Remove the 'active' class from all image list items in both award-img containers
      $(".award-img ul li").removeClass("active");

      // Add the 'active' class to the corresponding image list items in both award-img containers
      $(".award-img").each(function () {
        $(this)
          .find("ul li:eq(" + index + ")")
          .addClass("active");
      });
    },
  });

  // Home1 Solution Steps - stack + counter
  const ss = gsap.matchMedia();

  ss.add("(min-width: 992px)", () => {
    const section = document.querySelector(".home1-process-section");
    if (!section) return;

    const wrapper = section.querySelector(".process-wrapper");
    const cards = gsap.utils.toArray(
      section.querySelectorAll(".process-list .single-process"),
    );
    const countWrap = section.querySelector(".process-count");
    const countEl = countWrap?.querySelector("span");

    if (!wrapper || !cards.length || !countWrap || !countEl) return;

    const total = cards.length;
    const START_POS = "top 80px";

    // last card reference
    const lastCardST = ScrollTrigger.create({
      trigger: cards[total - 1],
      start: START_POS,
    });

    // init
    countEl.textContent = `1/${total}`;

    // ✅ pin the counter AND update number here (bidirectional)
    const counterST = ScrollTrigger.create({
      trigger: wrapper,
      start: START_POS,
      end: () => lastCardST.start,
      pin: countWrap,
      pinSpacing: false,
      anticipatePin: 1,
      invalidateOnRefresh: true,

      onUpdate: (self) => {
        // progress 0..1 => index 0..total-1 (works down & up)
        const idx = Math.min(
          total - 1,
          Math.max(0, Math.round(self.progress * (total - 1))),
        );
        countEl.textContent = `${idx + 1}/${total}`;
      },

      onLeave: () => {
        // optional: when leaving after last step, keep it at last number
        countEl.textContent = `${total}/${total}`;
      },
      onLeaveBack: () => {
        // optional: when scrolling back above section, reset to 1
        countEl.textContent = `1/${total}`;
      },
    });

    // cards stacking (no need onToggle for counter now)
    const cardSTs = cards.map((card) =>
      ScrollTrigger.create({
        trigger: card,
        start: START_POS,
        end: () => lastCardST.start,
        pin: true,
        pinSpacing: false,
        anticipatePin: 1,
        invalidateOnRefresh: true,
      }),
    );

    ScrollTrigger.refresh();

    // cleanup
    return () => {
      lastCardST.kill();
      counterST.kill();
      cardSTs.forEach((st) => st.kill());
      countEl.textContent = `1/${total}`;
    };
  });

  //Home4 Banner Video
  if (document.querySelector(".home4-banner-video video")) {
    const video = document.querySelector(".home4-banner-video video");
    const header = document.querySelector(
      "header.header-area, header.home4-sticky",
    );

    mm.add("(min-width: 991px)", () => {
      let stickyAdded = false;

      const tl = gsap.timeline({
        scrollTrigger: {
          trigger: ".home4-banner-video",
          start: "top 20%",
          endTrigger: ".home4-banner-video-full",
          end: "top top",
          scrub: true,
          pin: true,
          pinSpacing: false,
          invalidateOnRefresh: true,

          onEnter: () => {
            stickyLock = true; // ✅ disable global sticky
            header?.classList.remove("sticky"); // remove sticky immediately
            stickyAdded = false;
          },
          onEnterBack: () => {
            stickyLock = true;
            header?.classList.remove("sticky");
            stickyAdded = false;
          },

          onLeave: () => {
            // video section শেষ হয়ে গেলে আবার normal sticky চালু
            if (!stickyAdded) stickyLock = false;
          },
          onLeaveBack: () => {
            // উপরে ফিরে গেলে normal sticky চালু
            stickyLock = false;
          },

          onUpdate: () => {
            const currentWidth = video.getBoundingClientRect().width;
            const threshold = window.innerWidth * 0.95;

            // ✅ 95vw হলে sticky আবার চালু + class add
            if (currentWidth >= threshold && !stickyAdded) {
              stickyLock = false; // enable global sticky again
              header?.classList.add("sticky");
              stickyAdded = true;
            }

            // ✅ reverse scroll এ threshold এর নিচে গেলে আবার lock (video section এ থাকলে sticky off)
            if (currentWidth < threshold && stickyAdded) {
              stickyLock = true;
              header?.classList.remove("sticky");
              stickyAdded = false;
            }
          },
        },
      });

      tl.to(video, {
        width: "100vw",
        height: "100vh",
        y: () => {
          if (window.innerWidth >= 1600) return 100;
          if (window.innerWidth >= 992) return 40;
          return 60;
        },
        borderRadius: 0,
        ease: "none",
      });
    });
  }
})(jQuery);
