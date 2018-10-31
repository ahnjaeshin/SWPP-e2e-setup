import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Todo } from '../todo';
import { Observable, of } from 'rxjs';
import { map, tap, catchError } from 'rxjs/operators';

const httpOptions = {
  headers: new HttpHeaders({'Content-Type': 'application/json'})
};

@Injectable({
  providedIn: 'root'
})
export class TodoService {

  constructor(private http: HttpClient) { }
  // TODO
  getAllTodos(): Observable<Todo[]> {
    return this.http.get<Todo[]>('/api/todo')
      .pipe()
  }
  addTodo(todoContent): Observable<Todo> {
    const todo = {'content': todoContent}
    return this.http.post<Todo>('/api/todo', todo, httpOptions)
      .pipe()
  }
  updateTodo(todo) {
    const url = '/api/todo/' + todo.id
    return this.http.put<Todo>(url, todo, httpOptions)
      .pipe()
  }
  deleteTodoById(todoId) {
    const url = '/api/todo/' + todoId
    return this.http.delete(url)
      .pipe()
  }
}
