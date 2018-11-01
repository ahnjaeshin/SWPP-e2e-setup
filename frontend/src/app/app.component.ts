import { Component, OnInit } from '@angular/core';
import { TodoService } from './services/todo.service';
import { Todo } from './todo';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  todos: Todo[] = [];

  constructor(private todoService: TodoService) {}

  public ngOnInit() {
    this.todoService.getAllTodos().subscribe(
        (todos) => {
          this.todos = todos;
        }
      );
  }

  onAddTodo(todo) {
    this.todoService.addTodo(todo).subscribe(
        (newTodo) => {
          this.todos = this.todos.concat(newTodo);
        }
      );
  }

  onToggleTodo(todo: Todo) {
    this.todoService.updateTodo(todo).subscribe(
      () => {todo.done = !todo.done; });
  }

  onRemoveTodo(todo) {
    this.todoService.deleteTodoById(todo.id).subscribe(
        () => {
          this.todos = this.todos.filter((t) => t.id !== todo.id);
        }
      );
  }
}
