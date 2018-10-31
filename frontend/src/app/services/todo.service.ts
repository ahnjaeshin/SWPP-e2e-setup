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
    constructor(private http: HttpClient) { }

    getAllTodos(): Observable<Todo[]> {
        return this.http.get<Todo[]>("/api/todo/", httpOptions)
            .pipe(catchError(_ => of([])));
    }

    addTodo(content: string): Observable<Todo> {
        return this.http.post<Todo>('/api/todo/', { content: content, done: false }, httpOptions);
    }

    getTodoById(id: number): Observable<Todo> {
        return this.http.get<Todo>(`/api/todo/${id}/`, httpOptions)
    }

    updateTodo(todo: Todo): Observable<void> {
        return this.http.put<void>(`/api/todo/${todo.id}/`, todo, httpOptions)
    }

    deleteTodoById(id: number): Observable<void> {
        return this.http.delete<void>(`/api/todo/${id}/`, httpOptions)
    }
}
