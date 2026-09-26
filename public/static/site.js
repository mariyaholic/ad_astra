/* Progressive enhancement only: every page is complete without this file.
   - theme toggle (system -> light -> dark), remembered per browser
   - repository filter: text + type chips, synced to ?q=&type= for shareable views
   - copy buttons for checksums and citations */
(function () {
  "use strict";

  // ---------------------------------------------------------------- theme
  var root = document.documentElement;
  var toggle = document.querySelector("[data-theme-toggle]");
  function currentTheme() { return root.getAttribute("data-theme") || "system"; }
  function labelTheme() {
    if (!toggle) return;
    var t = currentTheme();
    toggle.textContent = "Theme: " + t;
    toggle.setAttribute("aria-label", "Colour theme: " + t + ". Activate to change.");
  }
  if (toggle) {
    toggle.hidden = false;
    labelTheme();
    toggle.addEventListener("click", function () {
      var next = { system: "light", light: "dark", dark: "system" }[currentTheme()];
      if (next === "system") root.removeAttribute("data-theme");
      else root.setAttribute("data-theme", next);
      try {
        if (next === "system") localStorage.removeItem("cygnus-theme");
        else localStorage.setItem("cygnus-theme", next);
      } catch (e) { /* not persisted; still applied for this page */ }
      labelTheme();
    });
  }

  // --------------------------------------------------------------- filter
  var form = document.querySelector("[data-filter]");
  if (form) {
    var rows = Array.prototype.slice.call(document.querySelectorAll("[data-filter-row]"));
    var input = form.querySelector("input[type=search]");
    var chips = Array.prototype.slice.call(form.querySelectorAll("[data-type]"));
    var count = document.querySelector("[data-result-count]");
    var empty = document.querySelector("[data-filter-empty]");
    var active = "all";
    form.hidden = false;

    var params = new URLSearchParams(window.location.search);
    if (params.get("q")) input.value = params.get("q");
    if (params.get("type") && chips.some(function (c) { return c.dataset.type === params.get("type"); })) {
      active = params.get("type");
    }

    function apply(push) {
      var q = input.value.trim().toLowerCase();
      var terms = q ? q.split(/\s+/) : [];
      var shown = 0;
      rows.forEach(function (row) {
        var hay = row.getAttribute("data-search");
        var okType = active === "all" || row.getAttribute("data-type") === active;
        var okText = terms.every(function (t) { return hay.indexOf(t) !== -1; });
        row.hidden = !(okType && okText);
        if (!row.hidden) shown++;
      });
      chips.forEach(function (c) { c.setAttribute("aria-pressed", String(c.dataset.type === active)); });
      if (count) count.textContent = shown + " of " + rows.length + " entries shown";
      if (empty) empty.hidden = shown !== 0;
      if (push) {
        var p = new URLSearchParams();
        if (q) p.set("q", input.value.trim());
        if (active !== "all") p.set("type", active);
        var qs = p.toString();
        history.replaceState(null, "", window.location.pathname + (qs ? "?" + qs : ""));
      }
    }
    input.addEventListener("input", function () { apply(true); });
    chips.forEach(function (c) {
      c.addEventListener("click", function () { active = c.dataset.type; apply(true); });
    });
    form.addEventListener("submit", function (e) { e.preventDefault(); apply(true); });
    apply(false);
  }

  // ----------------------------------------------------------------- copy
  document.querySelectorAll("[data-copy]").forEach(function (btn) {
    if (!navigator.clipboard) return;
    btn.hidden = false;
    btn.addEventListener("click", function () {
      var text = btn.getAttribute("data-copy");
      navigator.clipboard.writeText(text).then(function () {
        var old = btn.textContent;
        btn.textContent = "copied";
        btn.setAttribute("aria-live", "polite");
        setTimeout(function () { btn.textContent = old; }, 1400);
      }).catch(function () { /* clipboard blocked; value remains selectable */ });
    });
  });
})();
