import { Component, OnInit, Output, EventEmitter } from "@angular/core";
import { Todo } from "../todo";
import { TodoService } from "../services/todo.service";

@Component({
  selector: "app-todo-header",
  templateUrl: "./todo-header.component.html",
  styleUrls: ["./todo-header.component.css"]
})
export class TodoHeaderComponent implements OnInit {
  newContent = "";

  @Output() add: EventEmitter<string> = new EventEmitter();

  constructor(private todoService: TodoService) {}

  ngOnInit() {}

  addTodo() {
    let newTodo = { id: undefined, content: this.newContent, done: false };
    this.todoService.createTodo(newTodo).subscribe();
  }
}
