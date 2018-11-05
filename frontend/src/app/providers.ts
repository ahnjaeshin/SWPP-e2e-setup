import { Provider } from '@angular/core';
import { TodoService } from './services/todo.service';
import { todoServiceStub } from './services/todo-mock.service';

import { environment } from '../environments/environment';

export const TodoServiceProvider: Provider
 = (environment.useMock) ? {provide: TodoService, useValue: todoServiceStub}
                         : { provide: TodoService, useClass: TodoService };

export const APIUrlProvider: Provider = {provide: 'API_URL', useValue: environment.apiUrl};
