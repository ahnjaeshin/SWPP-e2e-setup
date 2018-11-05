import { Todo } from '../todo';
import { Observable, of } from 'rxjs';
import * as faker from 'faker';

let id = 0;

let mockTodoList = function(n: number) {
  const todos: Todo[] = [];
  const done = false;
  for (let i = 0; i < n; i++) {
    const content = faker.fake('{{lorem.sentence}}');
    todos.push({id, content, done});
    id++;
  }
  return todos;
}(5);

export const todoServiceStub = {

  addTodo: function(content: string): Observable<Todo> {
    const done = false;
    const new_todo = {id, content, done};
    return of(new_todo);
  },
  deleteTodoById: function(todoId: number): Observable<void> {
    mockTodoList = mockTodoList.filter(todo => todo.id !== todoId);
    return of(null);
  },
  updateTodo: function(todo: Todo): Observable<void> {
    const t: Todo = mockTodoList.find(_t => _t.id === todo.id);
    t.done = todo.done;
    t.content = todo.content;
    return of(null);
  },
  getAllTodos: function(): Observable<Todo[]> {
    return of(mockTodoList);
  },
  getTodoById: function(todoId: number): Observable<Todo> {
    const t: Todo = mockTodoList.find(_t => _t.id === todoId);
    return of(t);
  }
};
