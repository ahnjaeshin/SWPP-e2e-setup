import { Component, OnInit, Output, EventEmitter } from '@angular/core';

import { Todo } from '../todo';

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
    const content = this.newContent.trim();
    if (!content) return;
    this.add.emit(content);
    this.newContent = "";
  }
}
