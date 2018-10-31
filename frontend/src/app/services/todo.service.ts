import { Injectable } from "@angular/core";
import { HttpClient, HttpHeaders } from "@angular/common/http";

import { Todo } from "../todo";
import { Observable, of } from "rxjs";
import { map, tap, catchError } from "rxjs/operators";

@Injectable({
  providedIn: "root"
})
export class TodoService {
  constructor(private http: HttpClient) {}

  getTodos(): Observable<Todo[]> {
    return this.http.get<Todo[]>("http://localhost:8000/api/todo/");
  }

  createTodo(newTodo: Todo): Observable<Todo> {
    return this.http.post<Todo>("http://localhost:8000/api/todo/", newTodo);
  }

  getTodo(id: number): Observable<Todo> {
    return this.http.get<Todo>("http://localhost:8000/api/todo/" + id + "/");
  }

  deleteTodo(todo: Todo): Observable<Todo> {
    return this.http.delete<Todo>(
      "http://localhost:8000/api/todo/" + todo.id + "/"
    );
  }

  putTodo(newTodo: Todo): Observable<Todo> {
    return this.http.put<Todo>(
      "http://localhost:8000/api/todo/" + newTodo.id + "/",
      newTodo
    );
  }
}
