import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TodoFooterComponent } from './todo-footer.component';
import { Todo } from '../todo';

const mockTodoList: Todo[] = [
  { id: 1, content: 'Test1', done: false },
  { id: 2, content: 'Test2', done: true },
];

describe('TodoFooterComponent', () => {
  let component: TodoFooterComponent;
  let fixture: ComponentFixture<TodoFooterComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TodoFooterComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TodoFooterComponent);
    component = fixture.componentInstance;
    component.todos = mockTodoList;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
