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

  private todoUrl = 'api/todo/';

  constructor(
    private http: HttpClient
  ) { }

  getAllTodos(): Promise<Todo[]> {
    return this.http.get<Todo[]>(this.todoUrl)
    .pipe()
    .toPromise()
  }

  addTodo(todo: Todo): Promise<Todo> {
    return this.http.post<Todo>(this.todoUrl, todo, httpOptions)
    .pipe()
    .toPromise()
  }

  updateTodo(todo: Todo): Promise<Todo> {
    const url = `${this.todoUrl}${todo.id}/`;
    return this.http.put(url, todo, httpOptions)
    .pipe()
    .toPromise()
    .then(() => todo);
  }

  deleteTodoById(todoid: number): Promise<Todo> {
    const url = `${this.todoUrl}${todoid}/`;

    return this.http.delete<Todo>(url, httpOptions)
    .pipe()
    .toPromise()
  }
}
