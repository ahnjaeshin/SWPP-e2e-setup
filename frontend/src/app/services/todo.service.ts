import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Todo } from '../todo';
import { Observable, of } from 'rxjs';
import { map, tap, catchError } from 'rxjs/operators';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json'})
};
@Injectable({
  providedIn: 'root'
})
export class TodoService {
  todoURL = '/api/todo/'
  constructor(private http: HttpClient) { }
  getAllTodos() {
    return this.http.get<Todo[]>(this.todoURL)
  }
  addTodo(content: String) {
    const todo: Partial<Todo> = {
      content: content,
      done: false
    } as Partial<Todo>
    return this.http.post<Todo>(this.todoURL, todo, httpOptions)
  }
  getTodoById(id: number) {
    return this.http.get<Todo>(this.todoURL)
  }
  updateTodo(todo: Todo) {
    const url = `${this.todoURL}${todo.id}`
    return this.http.put<Todo>(url, todo, httpOptions)
  }
  deleteTodoById(todo: Todo| number) {
    const id = (typeof todo === 'number') ? todo : todo.id
    const url = `${this.todoURL}${id}`;
    return this.http.delete<Todo>(url, httpOptions)
  }
}
