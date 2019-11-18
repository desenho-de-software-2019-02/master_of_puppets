import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { NewRaceComponent } from './new-race.component';

describe('NewRaceComponent', () => {
  let component: NewRaceComponent;
  let fixture: ComponentFixture<NewRaceComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ NewRaceComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(NewRaceComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
