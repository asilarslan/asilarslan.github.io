(() => {
  const queryLanguage = new URLSearchParams(window.location.search).get("lang");
  const browserPrefersTurkish = (navigator.languages || [navigator.language || "en"])
    .some((language) => language.toLowerCase().startsWith("tr"));
  const initialLanguage = queryLanguage === "tr" || queryLanguage === "en"
    ? queryLanguage
    : (browserPrefersTurkish ? "tr" : "en");

  function setLanguage(language) {
    document.documentElement.lang = language;
    document.querySelectorAll("[data-language]").forEach((element) => {
      element.hidden = element.dataset.language !== language;
    });
    document.querySelectorAll("[data-set-language]").forEach((button) => {
      button.setAttribute("aria-pressed", String(button.dataset.setLanguage === language));
    });
  }

  document.querySelectorAll("[data-set-language]").forEach((button) => {
    button.addEventListener("click", () => setLanguage(button.dataset.setLanguage));
  });

  setLanguage(initialLanguage);
})();
