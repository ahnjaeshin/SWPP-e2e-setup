import { Component, OnInit } from '@angular/core';
import { TodoService } from './services/todo.service';
import { Todo } from './todo';
import {a} from '@angular/core/src/render3';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  todos: Todo[] = [];

  constructor(private todoService: TodoService) {}

  public async ngOnInit() {
    this.todos = await this.todoService.getAllTodos();
  }

  async onAddTodo(todo) {
    const newTodo = await this.todoService.addTodo(todo);
    this.todos = this.todos.concat(newTodo);
  }

  async onToggleTodo(todo: Todo) {
    const newTodo = await this.todoService.updateTodo(todo);
    newTodo.done = !newTodo.done;
  }

  async onRemoveTodo(todo) {
    await this.todoService.deleteTodoById(todo.id);
    this.todos = this.todos.filter((t) => t.id !== todo.id);
  }
}
