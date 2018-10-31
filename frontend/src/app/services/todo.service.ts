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

  list(): Observable<Todo[]> {
    return this.http.get('/api/todo/').pipe(map((opts: any[]) => opts.map(x => this.mapObj(x))));
  }

  get(id: number): Observable<Todo> {
    return this.http.get(`/api/todo/${id}`).pipe(map((opt: any) => this.mapObj(opt)));
  }

  save(resource: Todo): Observable<Todo> {
    let obs: Observable<any>;

    if (resource.id != null) {
      obs = this.http.put(`/api/todo/${resource.id}/`, resource, { headers: this.headers });
    } else {
      obs = this.http.post('/api/todo/', resource, { headers: this.headers });
    }
    return obs.pipe(map((opt: any) => this.mapObj(opt)));
  }

  delete(resource: Todo): Observable<void> {
    return this.http.delete(`/api/todo/${resource.id}/`).pipe(map((_: any) => null));
  }

  private mapObj(opt: any): Todo {
    return new Todo(opt);
  }

  private get headers(): HttpHeaders {
    return new HttpHeaders({'Content-Type': 'application/json'});
  }
}
