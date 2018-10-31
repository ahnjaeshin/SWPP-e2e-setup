import { TestBed, inject } from '@angular/core/testing';

import { TotoserviceService } from './totoservice.service';

describe('TotoserviceService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [TotoserviceService]
    });
  });

  it('should be created', inject([TotoserviceService], (service: TotoserviceService) => {
    expect(service).toBeTruthy();
  }));
});
