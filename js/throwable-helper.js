"use strict";

// Minimal extraction from Hub/egensThemes utilities (debounce only).
// Provides: window.egensDebounce (and the tiny helpers it depends on).

(function (window) {
  // --- internal helper (required by egensDebounce) ---
  const restArguments = function (func, startIndex) {
    return (
      (startIndex = startIndex == null ? func.length - 1 : +startIndex),
      function () {
        for (
          var length = Math.max(arguments.length - startIndex, 0),
            rest = Array(length),
            index = 0;
          index < length;
          index++
        ) {
          rest[index] = arguments[index + startIndex];
        }
        switch (startIndex) {
          case 0:
            return func.call(this, rest);
          case 1:
            return func.call(this, arguments[0], rest);
          case 2:
            return func.call(this, arguments[0], arguments[1], rest);
        }
        var args = Array(startIndex + 1);
        for (index = 0; index < startIndex; index++) args[index] = arguments[index];
        args[startIndex] = rest;
        return func.apply(this, args);
      }
    );
  };

  const egensDelay = restArguments(function (func, wait, args) {
    return setTimeout(function () {
      return func.apply(null, args);
    }, wait);
  });

  // --- egensDebounce (compatible with Hub utilities) ---
  window.egensDebounce = function (func, wait, immediate) {
    var timeout, result;

    var later = function (context, args) {
      timeout = null;
      if (args) result = func.apply(context, args);
    };

    var debounced = restArguments(function (args) {
      if (timeout) clearTimeout(timeout);

      if (immediate) {
        var callNow = !timeout;
        timeout = setTimeout(later, wait);
        if (callNow) result = func.apply(this, args);
      } else {
        timeout = egensDelay(later, wait, this, args);
      }

      return result;
    });

    debounced.cancel = function () {
      clearTimeout(timeout);
      timeout = null;
    };

    return debounced;
  };
})(window);
