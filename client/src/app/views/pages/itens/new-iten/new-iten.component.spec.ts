import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { NewItenComponent } from './new-iten.component';

describe('NewItenComponent', () => {
  let component: NewItenComponent;
  let fixture: ComponentFixture<NewItenComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ NewItenComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(NewItenComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
