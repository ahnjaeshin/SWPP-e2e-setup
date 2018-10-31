import { TestBed, inject, async, fakeAsync, tick } from '@angular/core/testing';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';

import { Observable } from 'rxjs';
import { Todo } from '../todo';

import { TodoService } from './todo.service';

const mockTodoList: Todo[] = [
  { id: 1, content: 'Test1', done: false },
  { id: 2, content: 'Test2', done: true },
];

const mockTodo: Todo = { id: 3, content: 'Test3', done: false };

describe('TodoService', () => {
  let httpClient: HttpClient;
  let httpTestingController: HttpTestingController;
  let todoService: TodoService;
  const todoApi = '/api/todo/';

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [TodoService]
    });
    httpClient = TestBed.get(HttpClient);
    httpTestingController = TestBed.get(HttpTestingController);
    todoService = TestBed.get(TodoService);
  });

  it('should be created', inject([TodoService], (service: TodoService) => {
    expect(service).toBeTruthy();
  }));

  it('should add todo with post request', async(() => {
    todoService.addTodo('Test3').subscribe(
      data => {expect(data).toEqual(mockTodo); });

    const req = httpTestingController.expectOne(todoApi);
    expect(req.request.method).toEqual('POST');
    req.flush(mockTodo);
  }));

  it('should delete todo with delete request', async(() => {
    const todoId = 1;
    const url = `${todoApi}/${todoId}`;

    todoService.deleteTodoById(todoId).subscribe();

    const req = httpTestingController.expectOne(url);
    expect(req.request.method).toEqual('DELETE');
    req.flush({});
  }));

  it('should update todo with PUT request', async(() => {
    const todoId = mockTodo.id;
    const url = `${todoApi}/${todoId}`;

    todoService.updateTodo(mockTodo).subscribe();

    const req = httpTestingController.expectOne(url);
    expect(req.request.method).toEqual('PUT');
    req.flush({});
  }));

  it('should get all todos with get request', async(() => {
    todoService.getAllTodos().subscribe(
      data => {expect(data).toEqual(mockTodoList); }
    );
    const req = httpTestingController.expectOne(todoApi);
    expect(req.request.method).toEqual('GET');
    req.flush(mockTodoList);
  }));

  it('should return empty list with get request if error', async(() => {
    todoService.getAllTodos().subscribe(
      data => {expect(data).toEqual([]); }
    );
    httpTestingController.expectOne(todoApi).flush(null, { status: 401, statusText: 'Unauthorized' });
  }));

  it('should get all todo of specific id with get request', async(() => {
    const todoId = mockTodo.id;
    const url = `${todoApi}/${todoId}`;

    todoService.getTodoById(todoId).subscribe(
      data => {expect(data).toEqual(mockTodo); }
    );
    const req = httpTestingController.expectOne(url);
    expect(req.request.method).toEqual('GET');
    req.flush(mockTodo);
  }));

  afterEach(() => {
    httpTestingController.verify();
  });
});
