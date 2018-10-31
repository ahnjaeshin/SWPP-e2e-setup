import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Todo } from './Todo';
import { tap } from 'rxjs/operators';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json'})
};

@Injectable({
  providedIn: 'root'
})
export class AppService {
  private todoURL = '/api/todo/';
  constructor(
    private http: HttpClient
  ) { }

  addTodo(todo: Todo) : Promise<Todo> {
    return this.http.post<Todo>(this.todoURL, todo, httpOptions)
      .pipe()
      .toPromise()
      .catch(this.handleError<Todo>('addTodo'));
  }

  getTodoList() : Promise<Todo[]> {
    return this.http.get<Todo[]>(this.todoURL)
      .toPromise()
      .catch(this.handleError<Todo[]>('getTodoList'))
  }

  getTodobyId(id: number) : Promise<Todo> {
    const url = `/api/todo/${id}/`;
    return this.http.get<Todo>(url)
      .toPromise()
      .catch(this.handleError<Todo>('getTodobyId'))
  }

  updateTodobyId(id:number, todo:Todo) : Promise<Todo> {
    const url = `/api/todo/${id}/`;
    return this.http.put<Todo>(url, todo, httpOptions)
      .toPromise()
      .catch(this.handleError<Todo>('updateTodobyId'))
  }

  deleteTodobyId(id:number) : Promise<void> {
    const url = `/api/todo/${id}/`;
    return this.http.delete<void>(url)
      .toPromise()
      .catch(this.handleError<void>('deleteTodobyId'))
  }

  private handleError<T> (operation = 'operation', result?: T) {
    return (error: any): Promise<T> => {

      console.error(error); // log to console instead
      // this.log(`${operation} failed: ${error.message}`);

      // Let the app keep running by returning an empty result.
      return Promise.resolve(result as T);
    };
  }
}
