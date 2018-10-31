export class Todo {
  id: number;
  content: string;
  done: boolean;

  constructor(opt: Todo) {
    Object.assign(this, opt);
  }
}
