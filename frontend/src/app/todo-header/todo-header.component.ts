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
    //app component로 올려줘야 함.
    //emit은 observable에 event를 넣어줌
    if (!this.newContent) {
      return;
    }
    this.add.emit(this.newContent);
    this.newContent = '';
  }

}
