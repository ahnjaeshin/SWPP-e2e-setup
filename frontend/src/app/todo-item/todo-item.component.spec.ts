import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TodoItemComponent } from './todo-item.component';
import { Todo } from '../todo';

const mockTodo: Todo = { id: 3, content: 'Test3', done: false };
describe('TodoItemComponent', () => {
  let component: TodoItemComponent;
  let fixture: ComponentFixture<TodoItemComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TodoItemComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TodoItemComponent);
    component = fixture.componentInstance;
    component.todo = mockTodo;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should emit toggled todo', () => {
    component.toggleComplete.subscribe(
      todo => expect(todo).toEqual(mockTodo)
    );
    component.toggleTodoComplete(mockTodo);
  });

  it('should remove todo', () => {
    component.remove.subscribe(
      todo => expect(todo).toEqual(mockTodo)
    );
    component.removeTodo(mockTodo);
  });
});
