odoo.define("manage.widget", function (require) {
  "use strict";

  const Widget = require("web.Widget");

  const MyWidget = Widget.extend({
    template: "my_widget_template",

    init: function () {
      this._super();

      // Inicializa el widget aquí.
      this.allowedCharacters = "0123456789CF";
    },

    renderElement: function () {
      // Renderiza el widget aquí.
      console.log("dentro de renderElement");
      return this.$el.html(
        `<input type="text" class="my-widget" value="${this.value}"/>`
      );
    },

    oninput: function () {
      // Valida el valor del campo en tiempo real.
      const value = this.$el.val();
      console.log("dentro de la funcion oninput");

      for (let i = 0; i < value.length; i++) {
        const character = value[i];

        if (!this.allowedCharacters.includes(character)) {
          value = value.substring(0, i) + value.substring(i + 1);
          break;
        }
      }

      this.$el.val(value);
    },
  });

  return MyWidget;
});
