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

  private todosUrl = '/api/todos'; //URL to web api

  constructor(private http: HttpClient) { }

  private todos: Todo[];

  getTodos (): Promise<Todo[]> {
    return this.http.get<Todo[]>(this.todosUrl)
      .toPromise()
      .then(todos =>{
        const newTodos = todos.filter(todo => todo.article_id === article_id)
        this.todos = newTodos;
        return newTodos;
      })
      .catch(this.handleError('getTodos', []));
  }
  // updateTodo
  createTodo (todo: Partial<Todo>): Promise<Todo> {
    return this.http.post<Todo>(this.todosUrl, todo, httpOptions)
    .toPromise()
    .catch(this.handleError<Todo>('createTodo'));
  }

  deleteTodo (todo: Todo | number): Promise<Todo> {
    const id = (typeof todo === 'number') ? todo : todo.id;
    const url = `${this.todosUrl}/${id}`;
    return this.http.delete<Todo>(url, httpOptions)
    .toPromise()
    .catch(this.handleError<Todo>('deleteTodo'));
  }

  updateTodo (todo: Todo): Promise<any> {
    const url = `${this.todosUrl}/${todo.id}`
    return this.http.put(url, todo, httpOptions).toPromise()
  }

  // Todo
  /*
   * Handle Http operation that failed.
   * Let the app continue.
   * @param operation - name of the operation that failed
   * @param result - optional value to return as the result
   */
  private handleError<T> (operation = 'operation', result?: T) {
    return (error: any): Promise<T> => {
      console.error(error); // log to console instead
      // Let the app keep running by returning an empty result.
      return Promise.resolve(result as T);
    };
  }

}
