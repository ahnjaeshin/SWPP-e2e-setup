import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Todo } from '../todo';
import { Observable, of } from 'rxjs';
import { map, tap, catchError } from 'rxjs/operators';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable({
  providedIn: 'root'
})
export class TodoService {

  todoUrl: string = '/api/toDo/'
  constructor(private http: HttpClient) { }

  /** HTTP GET METHOD **/
  getAllTodos(): Observable<Todo[]> {
    return this.http.get<Todo[]>(this.todoUrl)
  }

  getTodoById(id: number): Observable<Todo> {
    let todoIdUrl = this.todoUrl + id
    return this.http.get<Todo>(todoIdUrl)
  }

  /** HTTP POST METHOD **/
  addTodo(content: string): Observable<Todo> {
    let todo: Todo
    todo.content = content
    return this.http.post<Todo>(this.todoUrl, todo, httpOptions)
  }

  /** HTTP PUT METHOD **/
  updateTodo(todo: Todo): Observable<Todo> {
    let todoIdUrl = this.todoUrl + todo.id
    return this.http.put<Todo>(todoIdUrl, todo, httpOptions)
  }

  /** HTTP DELETE METHOD **/
  deleteTodoById(id: number): Observable<Todo> {
    let todoIdUrl = this.todoUrl + id
    return this.http.delete<Todo>(todoIdUrl, httpOptions)
  }
}
