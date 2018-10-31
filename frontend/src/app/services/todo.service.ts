import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Todo } from '../todo';
import { Observable, of } from 'rxjs';
import { map, tap, catchError } from 'rxjs/operators';

// TODO: ???????

@Injectable({
  providedIn: 'root'
})
export class TodoService {

  constructor(private http: HttpClient) { }

  // TODO:
  getAllTodos() {
    return this.http.get<Todo[]>("/api/todo/");
  }

  addTodo(todo : Todo) {
    console.log(todo);
    let obs = this.http.post<Todo>("/api/todo/", todo);
    obs.subscribe(console.log);
    return obs;
  }

  updateTodo(todo : Todo) {
    return this.http.put<Todo>("/api/todo/${todo.id}", todo);
  }

  deleteTodoById(id : number) {
    return this.http.delete<Todo>("/api/todo/${id}");
  }
}
