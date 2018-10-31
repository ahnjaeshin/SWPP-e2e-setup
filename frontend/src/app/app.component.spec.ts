import { TestBed, async, ComponentFixture, tick, fakeAsync } from '@angular/core/testing';
import { Component, Input, Output, EventEmitter } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { AppComponent } from './app.component';
import { TodoService } from './services/todo.service';

import { Todo } from './todo';
import { of, Observable } from 'rxjs';

const mockTodoList: Todo[] = [
  { id: 1, content: 'Test1', done: false },
  { id: 2, content: 'Test2', done: true },
];

const mockTodo: Todo = { id: 3, content: 'Test3', done: false };

@Component({selector: 'app-todo-list', template: ''})
class MockTodoListComponent {
  @Input() todos: Todo[];
  @Output() remove: EventEmitter<Todo> = new EventEmitter();
  @Output() toggleComplete: EventEmitter<Todo> = new EventEmitter();
}

@Component({selector: 'app-todo-header', template: ''})
class MockTodoHeaderComponent {
  @Output() add: EventEmitter<string> = new EventEmitter();
}

@Component({selector: 'app-todo-footer', template: ''})
class MockTodoFooterComponent {
  @Input() todos: Todo[];
}

describe('AppComponent', () => {
  let component: AppComponent;
  let fixture: ComponentFixture<AppComponent>;
  let todoService: jasmine.SpyObj<TodoService>;

  beforeEach(async(() => {
    const todoSpy = jasmine.createSpyObj('TodoService',
      ['addTodo', 'deleteTodoById', 'updateTodo', 'getAllTodos', 'getTodoById']);

    TestBed.configureTestingModule({
      imports: [
        FormsModule
      ],
      declarations: [
        AppComponent,
        MockTodoListComponent,
        MockTodoHeaderComponent,
        MockTodoFooterComponent,
      ],
      providers: [
        {provide: TodoService, useValue: todoSpy},
      ],
    }).compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AppComponent);
    component = fixture.componentInstance;
    todoService = TestBed.get(TodoService);
    todoService.getAllTodos.and.returnValue(of(mockTodoList));
    fixture.detectChanges();
  });

  it('should create the app', async(() => {
    expect(component).toBeTruthy();
  }));

  it('should retrieve all todos at ngOnInit', async(() => {
    todoService.getAllTodos.and.returnValue(of(mockTodoList));
    component.ngOnInit();
    expect(component.todos).toEqual(mockTodoList);
    expect(todoService.getAllTodos).toHaveBeenCalled();
  }));

  it('should be able to add new todo', async(() => {
    const mockTodoListChanged: Todo[] = [...mockTodoList];
    mockTodoListChanged.push(mockTodo);
    todoService.addTodo.and.returnValue(of(mockTodo));

    component.onAddTodo('Test3');
    fixture.detectChanges();
    expect(component.todos).toEqual(mockTodoListChanged);
    expect(todoService.addTodo).toHaveBeenCalled();
  }));

  it('should be able to toggle todos', async(() => {
    const mockTodoChanged: Todo = {...mockTodoList[0]};
    mockTodoChanged.done = true;
    todoService.updateTodo.and.returnValue(of(null));

    component.onToggleTodo(mockTodoChanged);
    fixture.detectChanges();

    expect(component.todos[0]).toEqual(mockTodoChanged);
    expect(todoService.updateTodo).toHaveBeenCalled();
  }));

  it('should be able to remove todos', async(() => {
    const mockTodoListChanged: Todo[] = mockTodoList.slice(1, 2);
    todoService.deleteTodoById.and.returnValue(of(null));

    component.onRemoveTodo(mockTodoList[0]);
    fixture.detectChanges();

    expect(component.todos).toEqual(mockTodoListChanged);
    expect(todoService.deleteTodoById).toHaveBeenCalled();
  }));
});
