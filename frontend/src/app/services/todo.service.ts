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

  async addTodo(content): Promise<Todo> {
    return await this.http.post<Todo>('/api/todo/', {content: content}).toPromise();
  }
  async deleteTodoById(id) {
    await this.http.delete(`/api/todo/${id}`).toPromise();
  }
  async updateTodo(todo): Promise<Todo> {
    return await this.http.put<Todo>(`/api/todo/${todo.id}`, todo).toPromise();
  }
  async getAllTodos(): Promise<Todo[]> {
    return await this.http.get<Todo[]>('/api/todo/').toPromise();
  }
  async getTodoById(id): Promise<Todo> {
    return await this.http.get<Todo>(`/api/todo/${id}/`).toPromise();
  }
}
