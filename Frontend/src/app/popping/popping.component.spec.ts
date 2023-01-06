import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PoppingComponent } from './popping.component';

describe('PoppingComponent', () => {
  let component: PoppingComponent;
  let fixture: ComponentFixture<PoppingComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PoppingComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PoppingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
