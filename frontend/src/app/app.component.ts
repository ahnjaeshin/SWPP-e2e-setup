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
    this.todoService.list().subscribe(
        (todos) => {
          this.todos = todos;
        }
      );
  }

  onAddTodo(content: string) {
    const todo = new Todo({
      id: null,
      done: false,
      content,
    });
    this.todoService.save(todo).subscribe(
        (newTodo) => {
          this.todos = this.todos.concat(newTodo);
        }
      );
  }

  onToggleTodo(todo: Todo) {
    todo.done = !todo.done;
    this.todoService.save(todo)
      .subscribe(() => { });
  }

  onRemoveTodo(todo) {
    this.todoService.delete(todo).subscribe(
        () => {
          this.todos = this.todos.filter((t) => t.id !== todo.id);
        }
      );
  }
}
