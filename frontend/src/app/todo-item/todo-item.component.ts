import { Component, OnInit, Input, Output, EventEmitter } from "@angular/core";
import { Todo } from "../todo";
import { TodoService } from "../services/todo.service";
@Component({
  selector: "app-todo-item",
  templateUrl: "./todo-item.component.html",
  styleUrls: ["./todo-item.component.css"]
})
export class TodoItemComponent implements OnInit {
  @Input() todo: Todo;

  @Output() remove: EventEmitter<Todo> = new EventEmitter();

  @Output() toggleComplete: EventEmitter<Todo> = new EventEmitter();

  constructor(private todoService: TodoService) {}

  ngOnInit() {}

  toggleTodoComplete(todo: Todo) {
    this.toggleComplete.emit(todo);
    todo.done = !todo.done;
    this.todoService.putTodo(todo).subscribe();
  }

  removeTodo(todo: Todo) {
    this.remove.emit(todo);
    this.todoService.deleteTodo(todo).subscribe();
  }
}
