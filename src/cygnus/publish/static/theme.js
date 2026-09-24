/* Loaded synchronously in <head> so a saved theme applies before first paint. */
(function () {
  try {
    var t = localStorage.getItem("cygnus-theme");
    if (t === "light" || t === "dark") document.documentElement.setAttribute("data-theme", t);
  } catch (e) { /* storage unavailable: follow the system setting */ }
})();
