import { Injectable, Inject } from '@angular/core';
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

  constructor(private http: HttpClient, @Inject('API_URL') private todoUrl: string) {}

  addTodo(content: string): Observable<Todo> {
    const payload = {content};
    return this.http.post<Todo>(this.todoUrl, payload, httpOptions)
      .pipe(catchError(this.handleError<Todo>('addTodo')));
  }

  deleteTodoById(todoId: number): Observable<void> {
    const url = `${this.todoUrl}${todoId}/`;

    return this.http.delete<void>(url, httpOptions)
      .pipe(catchError(this.handleError<void>('deleteTodo')));
  }

  updateTodo(todo: Todo): Observable<void> {
    const url = `${this.todoUrl}${todo.id}/`;
    return this.http.put(url, todo, httpOptions).pipe(
      tap(_ => this.log(`updated hero id=${todo.id}`)),
      catchError(this.handleError<any>('updateTodo'))
    );
  }

  getAllTodos(): Observable<Todo[]> {
    return this.http.get<Todo[]>(this.todoUrl)
      .pipe(catchError(this.handleError('getTodo', [])));
  }

  getTodoById(todoId: number): Observable<Todo> {
    const url = `${this.todoUrl}${todoId}/`;
    return this.http.get<Todo>(url)
      .pipe(catchError(this.handleError<Todo>(`getTodo id=${todoId}`))
    );
  }

  /** Log a HeroService message with the MessageService */
  private log(message: string) {
    console.log(`TodoService: ${message}`);
  }

  private handleError<T> (operation = 'operation', result?: T) {
    return (error: any): Promise<T> => {

      console.error(error); // log to console instead
      this.log(`${operation} failed: ${error.message}`);

      // Let the app keep running by returning an empty result.
      return Promise.resolve(result as T);
    };
  }
}
