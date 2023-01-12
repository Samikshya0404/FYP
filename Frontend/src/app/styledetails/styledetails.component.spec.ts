import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StyledetailsComponent } from './styledetails.component';

describe('StyledetailsComponent', () => {
  let component: StyledetailsComponent;
  let fixture: ComponentFixture<StyledetailsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ StyledetailsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(StyledetailsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
