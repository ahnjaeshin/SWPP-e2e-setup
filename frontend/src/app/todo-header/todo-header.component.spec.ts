import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { FormsModule } from '@angular/forms';
import { TodoHeaderComponent } from './todo-header.component';
import { Todo } from '../todo';

describe('TodoHeaderComponent', () => {
  let component: TodoHeaderComponent;
  let fixture: ComponentFixture<TodoHeaderComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [ FormsModule ],
      declarations: [ TodoHeaderComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TodoHeaderComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should not emit event if header is empty', () => {
    component.add.subscribe(content => {
      expect(content).toBeFalsy();
    });
    component.newContent = '';
    component.addTodo();
  });
  it('should not emit event if header is empty', () => {
    const newContent = 'Test3';
    component.add.subscribe(content => {
      expect(content).toBeTruthy();
      expect(content).toEqual(newContent);
    });
    component.newContent = newContent;
    component.addTodo();
  });
});
