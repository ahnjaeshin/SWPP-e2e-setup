import { Component, OnInit } from "@angular/core";
import { TodoService } from "./services/todo.service";
import { Todo } from "./todo";

@Component({
  selector: "app-root",
  templateUrl: "./app.component.html",
  styleUrls: ["./app.component.css"]
})
export class AppComponent implements OnInit {
  todos: Todo[] = [];

  constructor(private todoService: TodoService) {}

  public ngOnInit() {
    this.todoService.getTodos().subscribe(todos => {
      this.todos = todos;
    });
  }

  onAddTodo(todo) {
    this.todoService.createTodo(todo).subscribe(newTodo => {
      this.todos = this.todos.concat(newTodo);
    });
  }

  onToggleTodo(todo: Todo) {
    this.todoService.putTodo(todo).subscribe(() => {
      todo.done = !todo.done;
    });
  }

  onRemoveTodo(todo) {
    this.todoService.deleteTodo(todo).subscribe(() => {
      this.todos = this.todos.filter(t => t.id !== todo.id);
    });
  }
}
