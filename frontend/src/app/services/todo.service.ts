import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Todo } from '../todo';
import { Observable, of } from 'rxjs';
import { map, tap, catchError } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class TodoService {

  constructor(private http: HttpClient) { }

  host = "http://localhost:8080"

  getAllTodos(): Observable<Todo[]> {
    return this.http.get<Todo[]>(this.host + '/api/todo/');
  }

  addTodo(todo: Todo) {
    return this.http.post<Todo>(this.host + '/api/todo', {...todo});
  }

  updateTodo(todo: Todo) {
    return this.http.put(this.host + `/api/todo/${todo.id}/`, {...todo});
  }

  deleteTodoById(todo: Todo) {
    return this.http.delete(this.host + `/api/todo/${todo.id}/`);
  }

}
