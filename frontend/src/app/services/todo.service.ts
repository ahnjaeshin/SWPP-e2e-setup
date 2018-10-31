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
//???
  getAllTodos(){
    return null
  }
  addTodo(todo:Todo){
    return null
  }
  updateTodo(todo:Todo){
    return null
  }
  deleteTodoById(id:number){
    return null
  }
}
