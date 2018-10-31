import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Todo } from '../todo';
import { Observable, of } from 'rxjs';
import { map, tap, catchError } from 'rxjs/operators';

???????

@Injectable({
  providedIn: 'root'
})
export class TodoService {

  constructor(private http: HttpClient) { }

  ???????
}
