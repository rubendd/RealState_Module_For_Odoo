/** @odoo-module **/

import { registry } from "@web/core/registry";
const { Component, useState, onWillStart } = owl;
import { useService } from "@web/core/utils/hooks";

export class OwlTodoList extends Component {
  setup() {
    this.state = useState({
      tasklist: [],
    });
    this.orm = useService("orm");
    this.model = "owl.todo";

    onWillStart(async () => {
      await this.getAllTask();
    });
  }
  async getAllTask() {
    this.state.tasklist = await this.orm.searchRead(
      this.model,
      [],
      ["name", "color", "completed"]
    );
  }
}

OwlTodoList.template = "owl.TodoList";

registry.category("actions").add("owl.action_todo_list_js", OwlTodoList);
