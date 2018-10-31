import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Todo } from '../todo';
import { Observable, of } from 'rxjs';
import { map, tap, catchError } from 'rxjs/operators';

const httpOptions = {
	headers: new HttpHeaders({ 'Content-Type': 'application/json' })
}

@Injectable({
  providedIn: 'root'
})
export class TodoService {

  constructor(private http: HttpClient) { }

  private todosUrl: string = '/api/todo/';

  getAllTodos(): Promise<Todo[]> {
  	return this.http.get<Todo[]>(this.todosUrl)
  	  .pipe(tap(todos => this.log('fetched todos')))
  	  .toPromise()
  	  .catch(this.handleError('getTodos', [])));
  }

  getTodo(id: number): Promise<Todo> {
  	const url = this.todosUrl + id;
  	return this.http.get<Todo>(url)
  	  .pipe(tap(_ => this.log('fetched todo id = ' + id)))
  	  .toPromise()
  	  .catch(this.handleError<Todo>('getTodo id = ' + id));
  }

  addTodo(todo: Todo): Promise<Todo> {
  	return this.http.post<Todo>(this.todosUrl, todo, httpOptions)
  	  .pipe(tap((newTodo: Todo) => this.log('added todo with id= ' + newTodo.id)))
  	  .toPromise()
  	  .catch(this.handleError<Todo>('addTodo'));
  }

  updateTodo(todo: Todo): Promise<Todo> {
  	const url = '/api/todo/' + todo.id;
  	return this.http.put(url, todo, httpOptions)
  	  .pipe(tap(_ => this.log('updated todo id = ' + todo.id)))
  	  .toPromise()
  	  .then(() => todo)
  	  .catch(this.handleError<any>('updateUser'));
  }

  deleteTodoById(todo: Todo | number): Promise<Todo> {
  	const id = (typeof todo === 'number') ? todo : todo.id;
  	const url = this.todosUrl + id;
  	return this.http.delete<Todo>(url, httpOptions)
  	  .pipe(tap(_ => this.log('deleted todo id = ' + id)))
  	  .toPromise()
  	  .catch(this.handleError<Todo>('deleteTodo'));
  }

  private log(message: string) {
  	console.log('UserService: ' + message);
  }

  private handleError<T> (operation = 'operation', result?: T) {
  	return (error: any): Promise<T> => {
  	  console.error(error);
  	  this.log(operation + " failed: " + error.message);
  	  return Promise.resolve(result as T);
  	}
  }
}
