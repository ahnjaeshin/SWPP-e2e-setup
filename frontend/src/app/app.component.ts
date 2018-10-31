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
    this.todoService.getAllTodos().then(
        (todos) => {
          this.todos = todos;
        }
      );
  }

  onAddTodo(todo) {
    this.todoService.addTodo(todo).then(
        (newTodo) => {
          this.todos = this.todos.concat(newTodo);
        }
      );
  }

  onToggleTodo(todo: Todo) {
    this.todoService.updateTodo(todo).then(
      () => {todo.done = !todo.done; });
  }

  onRemoveTodo(todo) {
    this.todoService.deleteTodoById(todo.id).then(
        () => {
          this.todos = this.todos.filter((t) => t.id !== todo.id);
        }
      );
  }
}
