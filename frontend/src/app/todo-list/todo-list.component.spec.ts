import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { Component, Input, Output, EventEmitter } from '@angular/core';
import { TodoListComponent } from './todo-list.component';
import { Todo } from '../todo';

const mockTodoList: Todo[] = [
  { id: 1, content: 'Test1', done: false },
  { id: 2, content: 'Test2', done: true },
];

const mockTodo: Todo = { id: 3, content: 'Test3', done: false };


@Component({selector: 'app-todo-item', template: ''})
export class MockTodoItemComponent {
  @Input() todo: Todo;
  @Output() remove: EventEmitter<Todo> = new EventEmitter();
  @Output() toggleComplete: EventEmitter<Todo> = new EventEmitter();

  toggleTodoComplete(todo: Todo) {
    this.toggleComplete.emit(todo);
  }

  removeTodo(todo: Todo) {
    this.remove.emit(todo);
  }
}
describe('TodoListComponent', () => {
  let component: TodoListComponent;
  let fixture: ComponentFixture<TodoListComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [
        TodoListComponent,
        MockTodoItemComponent
      ],
    }).compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TodoListComponent);
    component = fixture.componentInstance;
    component.todos = mockTodoList;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should emit toggled todo', () => {
    component.toggleComplete.subscribe(
      todo => expect(todo).toEqual(mockTodo)
    );
    component.onToggleTodoComplete(mockTodo);
  });

  it('should remove todo', () => {
    component.remove.subscribe(
      todo => expect(todo).toEqual(mockTodo)
    );
    component.onRemoveTodo(mockTodo);
  });
});
