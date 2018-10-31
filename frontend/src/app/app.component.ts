import { Component } from '@angular/core';
import { Todo } from "./Todo";
import { AppService } from "./app-service.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app';
  todos: Todo[];
  content: string;

  constructor(
    private appService: AppService,
  ) { }

  ngOnInit() {
    this.appService.getTodoList()
      .then(list => this.todos = list);
  }

  onClickAdd(){
    let todo = new Todo();
    todo.content = this.content;
    todo.done = false;
    this.appService.addTodo(todo)
      .then(newTodo => this.todos.push(newTodo));
  }

  onClickDelete(id:number){
    this.appService.deleteTodobyId(id)
      .then( () => this.todos = this.todos.filter(todo => todo.id != id))
  }
}
