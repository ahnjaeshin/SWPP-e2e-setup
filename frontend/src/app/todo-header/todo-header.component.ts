import { Component, OnInit, Output, EventEmitter } from '@angular/core';


@Component({
  selector: 'app-todo-header',
  templateUrl: './todo-header.component.html',
  styleUrls: ['./todo-header.component.css']
})
export class TodoHeaderComponent implements OnInit {

  newContent = '';

  @Output()
  add: EventEmitter<string> = new EventEmitter();

  constructor() { }

  ngOnInit() {
  }

  addTodo() {
    this.add.emit(this.newContent)
  }

}
