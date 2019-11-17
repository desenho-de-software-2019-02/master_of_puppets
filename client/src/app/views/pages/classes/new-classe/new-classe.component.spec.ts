import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { NewClasseComponent } from './new-classe.component';

describe('NewClasseComponent', () => {
  let component: NewClasseComponent;
  let fixture: ComponentFixture<NewClasseComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ NewClasseComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(NewClasseComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
